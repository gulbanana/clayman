from collections import defaultdict
import numbers
import re
import bs4
from . import site
import _settings

class Quality:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class Character:
    def __init__(self, username, password):
        self.game = site.Browser()

        # this uselessly returns the same thing as /Storylet/Available, inner html only
        self.game.post('/Auth/EmailLogin', {'emailAddress': username, 'password': password})
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
        if not isinstance(item, Quality):
            item = self._items_by_id[item]

        html = self.game.post('/Storylet/UseQuality', {'qualityId': item.id})
        soup = bs4.BeautifulSoup(html)

        self._parse_branches(soup)
        print('Used {0}'.format(item.name))

    def begin_story(self, storylet):
        if not isinstance(storylet, numbers.Number):
            try:
                storylet = self.storylets[storylet]
            except KeyError:
                self._debug()
                raise

        html = self.game.post('/Storylet/Begin', {'eventid': storylet})
        soup = bs4.BeautifulSoup(html)

        self._parse_branches(soup)
        title = soup.h3.string.strip()
        print('"{0}"'.format(title))

    def choose_branch(self, branch, second_chance=False):
        if not isinstance(branch, numbers.Number):
            try:
                branch = self.branches[branch]
                print('--> {0}'.format(branch))
            except KeyError:
                self._debug()
                raise

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
        self.actions = int(match.group(1))

        effects = soup.find('div', class_='quality_update_box').find_all('p')
        for tag in effects:
            content = ''.join(tag.strings)
            if not 'You succeeded' in content:
                print('    {0}'.format(content))

            inner_match = re.match(r'(.+) has (increased|dropped) to (\d+)', content)
            if inner_match:
                qname, qval = inner_match.group(1,3)
                self.qualities[qname] = int(qval)

            inner_match = re.match(r'An occurrence! Your \'(.+)\' quality is now (\d+)', content)
            if inner_match:
                qname, qval = inner_match.group(1,2)
                self.qualities[qname] = int(qval)

            inner_match = re.match(r'(.+) has been reset', content)
            if inner_match:
                qname = inner_match.group(1)
                self.qualities[qname] = 0

            inner_match = re.match(r'You\'ve (gained|lost) (\d+) x (.+) \(new total (\d+)\)', content)
            if inner_match:
                iname, ival = inner_match.group(3,4)
                self.items[iname] = int(ival)

            inner_match = re.match(r'You now have (\d+) x (.+)', content)
            if inner_match:
                iname, ival = inner_match.group(2,1)
                self.items[iname] = int(ival)

            inner_match = re.match(r'You no longer have any of this: \'(.+)\'', content)
            if inner_match:
                iname = inner_match.group(1)
                self.items[iname] = 0

    def _update_status(self):
        outer_html = self.game.get('/Gap/Load', dict(content='/Me'))
        outer_soup = bs4.BeautifulSoup(outer_html)

        self._update_status_inner(outer_soup)

    def _update_status_inner(self, outer_soup):
        inner_html = self.game.post('/Me', dict())
        inner_soup = bs4.BeautifulSoup(inner_html)

        action_tag = outer_soup.find('span', class_='actions_remaining')
        self.actions = int(action_tag.contents[0].string)
        self.action_cap = int(action_tag.contents[1][1:])

        area_tag = outer_soup.find('div', id='currentAreaSection')
        match = re.search(r'displayCurrentArea\((\d+)', area_tag.script.string)
        self.location = int(match.group(1))

        def stat(id):
            level = outer_soup.find('span', id='infoBarQLevel'+str(id))
            bonus = outer_soup.find('span', id='infoBarBonusPenalty'+str(id))
            expression = level.string
            if bonus.string:
                expression += bonus.string
            return eval(expression)

        self.watchful = stat(209)
        self.shadowy = stat(210)
        self.dangerous = stat(211)
        self.persuasive = stat(212)

        self.qualities = defaultdict(int)
        quals = inner_soup.find('div', class_='you_bottom_lhs')
        for quality in [q.string for q in quals('strong') if q.string]:
            matches = re.search(r'(.*) (\d+)', quality.string)
            if matches:
                name = matches.group(1)
                quantity = int(matches.group(2))
                self.qualities[name] = int(quantity)

        self._items_by_id = dict()
        self.items = defaultdict(int)
        equipment = inner_soup.find('div', id='inventory')
        possessions = inner_soup.find('div', class_='you_bottom_rhs')
        for item in [possession for possession in  possessions('li') if len(possession.a.contents) > 0]:
            tooltip = item.a['title']
            matches = re.search(r'>(\d+) x (.*?)<', tooltip)
            name = matches.group(2)
            quantity = int(matches.group(1))

            imagediv = item('div')[1]['id']
            match = re.search(r'infoBarQImage(\d+)', imagediv)
            id = match.group(1)

            self._items_by_id[name] = Quality(id, name, quantity)
            self.items[name] = quantity

        heading = inner_soup.find('div', class_='redesign_heading')
        self.name = heading.h1.a.string
        self.description = ' '.join(heading.p.stripped_strings)
        print('{0}: {1}.'.format(self.name, self.description))

    def _debug(self):
        print('### REST api status at time of error ###')
        print('# available storylets: ' + repr(self.storylets))
        print('# available branches: ' + repr(self.branches))