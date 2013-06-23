from london import *

character = Gentleperson()

character.travel(areas.Veilgarden)

# +54 whispered secrets per action
for i in range(0,6):
    character.begin_story('The demands of high society')
    character.choose_branch('Attend an event')
    character.onwards()