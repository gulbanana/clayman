from london import *

# Elder

def jade_persuasive(character):
    """+75 jade (0.75E)
    max persuasive: 88
    failure: scandal"""
    character.travel(areas.SHUTTERED_PALACE)
    character.begin_story('Become a trader in antiques')
    character.choose_branch('Deal in pretty trinkets')
    character.onwards()

def jade_watchful(character):
    """+82 jade fragments (0.82E)
    failure: 2cp scandal"""
    character.travel(areas.FORGOTTEN_QUARTER)
    character.begin_story('A tour of the quarter')
    character.choose_branch('The exploitation of knowledge')
    character.onwards()

# Infernal

def souls(character):
    """+28 soul (0.56E)
    also has a Shadowy option"""
    character.travel(areas.LADYBONES_ROAD)
    character.begin_story('Track down a Spirifer')
    character.choose_branch('Watch from the rooftops')

# Mysteries

def cryptic_clues(character):
    """+30 cryptic clues (0.60E)"""
    character.travel(areas.VEILGARDEN)
    character.begin_story('Correspond with a contact at the Shuttered Palace')
    character.choose_branch('Write a letter')
    character.onwards()

def cryptic_clues_watchful(character):
    """+39 cryptic clues (0.78E)"""
    character.travel(areas.FORGOTTEN_QUARTER)
    character.begin_story('Understanding the Correspondence')
    character.choose_branch('A distinctly cautious approach')
    character.onwards()

def whispered_secrets(character):
    """+54 whispered secrets per action (0.54E)"""
    character.travel(areas.VEILGARDEN)
    character.begin_story('The demands of high society')
    character.choose_default_branch()
    character.onwards()

# Rumour

def proscribed_material(character):
    """+54 whispered secrets per action (0.54E)"""
    character.travel(areas.VEILGARDEN)
    character.begin_story('Charm an influential social butterfly')
    character.choose_default_branch()
    character.onwards()

# Wines

def greyfields_1882(character):
    """+37 Greyfields 1882 (0.74E)
    scandal on failure
    max persuasive 84 (72% chance)"""
    character.travel(areas.SHUTTERED_PALACE)
    character.begin_story('The Antiquarian Footman')
    character.choose_branch('Offer the fellow a partnership')
    character.onwards()