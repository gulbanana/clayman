from . import site

def travel(area):
    print('Travelling to {0}'.format(area.__name__))
    site.command('/Map/Move', {'areaid': area._id})

def use_item(item):
    print('Using {0}'.format(item.__name__))
    site.command('/Storylet/UseQuality', {'qualityId': item._id})

    if hasattr(item, 'default'):
        global default_branch
        default_branch = item.default

def begin_story(storylet):
    print('Beginning {0}'.format(storylet.__name__))
    site.command('/Storylet/Begin', {'eventid': storylet._id})

    if hasattr(storylet, 'default'):
        global default_branch
        default_branch = storylet.default

def choose_default():
    global default_branch
    choose_branch(default_branch)

def choose_branch(branch):
    site.command('/Storylet/ChooseBranch', {'branchid': branch})