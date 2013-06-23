import london

character = london.Gentleperson()
character.travel(london.areas.Lodgings)
print('Actions available: {0}/{1}'.format(character.actions, character.action_cap))