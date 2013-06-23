import london

character = london.Gentleperson()

character.travel(london.areas.Veilgarden)

for i in range(0,6):
    character.begin_story(london.areas.Veilgarden.demands_of_high_society)
    character.choose_default_branch()
