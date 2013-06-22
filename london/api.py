import bs4
from . import site

def travel(area):
    site.command('/Map/Move', {'areaid': area._id})
    print('Welcome to {0}, delicious friend!'.format(area.__name__))


def use_item(item):
    html = site.command('/Storylet/UseQuality', {'qualityId': item._id})
    soup = bs4.BeautifulSoup(html)
    print('Used {0}'.format(item.__name__))

    if hasattr(item, 'default'):
        global default_branch
        default_branch = item.default


def begin_story(storylet):
    html = site.command('/Storylet/Begin', {'eventid': storylet._id})
    soup = bs4.BeautifulSoup(html)
    print('"{0}"'.format(soup.h3.string.strip()))

    if hasattr(storylet, 'default'):
        global default_branch
        default_branch = storylet.default


def choose_branch(branch):
    html = site.command('/Storylet/ChooseBranch', {'branchid': branch})
    soup = bs4.BeautifulSoup(html)
    effects = soup.find_all('p')

    for tag in effects[1:]:
        content = ''.join(tag.strings)
        if not 'You succeeded' in content:
            print(content)


def choose_default():
    global default_branch
    choose_branch(default_branch)