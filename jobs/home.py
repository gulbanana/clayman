from london import *

character = Gentleperson()
character.travel(areas.Lodgings)
print('Actions available: {0}/{1}'.format(character.actions, character.action_cap))