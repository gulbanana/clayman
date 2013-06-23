import bs4
from . import site

actions = 0
action_cap = 10

def update():
    html = site.get('/Gap/Load', dict(content='/Me'))
    soup = bs4.BeautifulSoup(html)

    global actions, action_cap
    action_tag = soup.find('span', class_='actions_remaining')
    actions = action_tag.contents[0].string
    action_cap = action_tag.contents[1][1:]

    print('Updated my journal.')

update()
