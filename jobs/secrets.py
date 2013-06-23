from london import *

character = Gentleperson()

character.travel(areas.Veilgarden)

# +54 whispered secrets per action
for i in range(0,6):
    character.begin_story(areas.Veilgarden.demands_of_high_society)
    character.choose_default_branch()