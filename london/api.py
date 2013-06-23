import numbers
import bs4
from . import site
import _settings

class Gentleperson:
    def __init__(self):
        self.game = site.Browser(_settings.AUTH_USER, _settings.AUTH_PASS)
        print('Entered the Neath.')
        self._update_status()

    def travel(self, area):
        html = self.game.post('/Map/Move', {'areaid': area._id})
        soup = bs4.BeautifulSoup(html)

        self._parse_branches(soup)

        print('Welcome to {0}, delicious friend!'.format(area.__name__))

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

        # XXX there can be more than one descriptive para, find a better way
        effects = soup.find_all('p')
        for tag in effects[1:]:
            content = ''.join(tag.strings)
            if not 'You succeeded' in content:
                print('    {0}'.format(content))

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
        html = self.game.get('/Gap/Load', dict(content='/Me'))
        soup = bs4.BeautifulSoup(html)

        action_tag = soup.find('span', class_='actions_remaining')
        self.actions = action_tag.contents[0].string
        self.action_cap = action_tag.contents[1][1:]

        print('Updated my journal.')

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
