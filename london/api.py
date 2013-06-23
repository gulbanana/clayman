import numbers
import re
import bs4
from . import site
import _settings

class Gentleperson:
    def __init__(self, username, password):
        self.game = site.Browser(username, password)
        print('Entered the Neath.')
        self._update_status()

    def travel(self, area):
        if self.location == area.id:
            if not hasattr(self, 'storylets'):
                html = self.game.post('/Storylet/Available', {})
                soup = bs4.BeautifulSoup(html)
                self._parse_branches(soup)
            return

        html = self.game.post('/Map/Move', {'areaid': area.id})
        soup = bs4.BeautifulSoup(html)

        self.location = area.id
        self._parse_branches(soup)
        print('Welcome to {0}, delicious friend!'.format(area.name))

    def use_item(self, item):
        html = self.game.post('/Storylet/UseQuality', {'qualityId': item._id})
        soup = bs4.BeautifulSoup(html)

        self._parse_branches(soup)
        print('Used {0}'.format(item.__name__))

    def begin_story(self, storylet):
        if not isinstance(storylet, numbers.Number):
            storylet = self.storylets[storylet]

        html = self.game.post('/Storylet/Begin', {'eventid': storylet})
        soup = bs4.BeautifulSoup(html)

        self._parse_branches(soup)
        title = soup.h3.string.strip()
        print('"{0}"'.format(title))

    def choose_branch(self, branch, second_chance=False):
        if not isinstance(branch, numbers.Number):
            print('--> {0}'.format(branch))
            branch = self.branches[branch]

        html = self.game.post('/Storylet/ChooseBranch', dict(branchid=branch, secondChances=second_chance))
        soup = bs4.BeautifulSoup(html)
        self._parse_effects(soup)

    def choose_default_branch(self):
        if len(self.branches) != 1:
            raise Exception('More than one branch is available.')

        self.choose_branch(next(iter(self.branches.keys())))

    def perhaps_not(self):
        html = self.game.post('/Storylet/GoBackFromStorylet', {})
        soup = bs4.BeautifulSoup(html)
        self._parse_branches(soup)
        print('--> Perhaps not.')

    def onwards(self):
        html = self.game.post('/Storylet/Available', {})
        soup = bs4.BeautifulSoup(html)
        self._parse_branches(soup)
        print('--> Onwards!')

    def _update_status(self):
        outer_soup = bs4.BeautifulSoup(self.game.get('/Gap/Load', dict(content='/Me')))
        inner_soup = bs4.BeautifulSoup(self.game.post('/Me', dict()))

        action_tag = outer_soup.find('span', class_='actions_remaining')
        self.actions = int(action_tag.contents[0].string)
        self.action_cap = int(action_tag.contents[1][1:])

        area_tag = outer_soup.find('div', id='currentAreaSection')
        match = re.search(r'displayCurrentArea\((\d+)', area_tag.script.string)
        self.location = int(match.groups(0)[0])

        heading_tag = inner_soup.find('div', class_='redesign_heading')
        self.name = heading_tag.h1.a.string
        self.description = ' '.join(heading_tag.p.stripped_strings)

        print('{0}: {1}.'.format(self.name, self.description))

    def _parse_branches(self, soup):
        self.branches = dict()
        self.storylets = dict()
        for tag in soup.find_all('div', class_='storylet'):
            if tag.contents[1].name == 'form':  #branch
                title = tag.contents[1].contents[3].contents[1].string.strip()
                form = tag.contents[1]
                self.branches[title] = form['onsubmit'][64:].split(',')[0]
            else:                               #storylet
                title = tag.contents[3].contents[1].string.strip()
                button = tag.contents[5].contents[1].contents[1]
                self.storylets[title] = button['onclick'][11:][:-2]

    def _parse_effects(self, soup):
        update_script = soup.find_all('script')[1].string
        match = re.search(r'setActionsLevel\((\d+)', update_script)
        self.actions = int(match.groups(0)[0])

        # XXX there can be more than one descriptive para, find a better way
        effects = soup.find_all('p')
        for tag in effects[1:]:
            content = ''.join(tag.strings)
            if not 'You succeeded' in content:
                print('    {0}'.format(content))


