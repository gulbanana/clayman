import bs4
from . import site
import _settings

class Gentleperson:
    def __init__(self):
        self.game = site.Browser(_settings.AUTH_USER, _settings.AUTH_PASS)
        print('Entered the Neath.')
        self.update_status()

    def travel(self, area):
        self.game.post('/Map/Move', {'areaid': area._id})
        print('Welcome to {0}, delicious friend!'.format(area.__name__))

    def use_item(self, item):
        html = self.game.post('/Storylet/UseQuality', {'qualityId': item._id})
        soup = bs4.BeautifulSoup(html)
        print('Used {0}'.format(item.__name__))

        if hasattr(item, 'default'):
            self.default_branch = item.default

    def begin_story(self, storylet):
        html = self.game.post('/Storylet/Begin', {'eventid': storylet._id})
        soup = bs4.BeautifulSoup(html)
        print('"{0}"'.format(soup.h3.string.strip()))

        if hasattr(storylet, 'default'):
            self.default_branch = storylet.default

    def choose_branch(self, branch):
        html = self.game.post('/Storylet/ChooseBranch', {'branchid': branch})
        soup = bs4.BeautifulSoup(html)
        effects = soup.find_all('p')

        for tag in effects[1:]:
            content = ''.join(tag.strings)
            if not 'You succeeded' in content:
                print(content)

    def choose_default_branch(self):
        self.choose_branch(self.default_branch)

    def update_status(self):
        html = self.game.get('/Gap/Load', dict(content='/Me'))
        soup = bs4.BeautifulSoup(html)

        action_tag = soup.find('span', class_='actions_remaining')
        self.actions = action_tag.contents[0].string
        self.action_cap = action_tag.contents[1][1:]

        print('Updated my journal.')