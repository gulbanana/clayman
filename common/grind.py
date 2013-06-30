from london import *

def grind_jade(character):
    """+75 jade (0.75E)
    scandal on failure"""
    character.travel(areas.SHUTTERED_PALACE)
    character.begin_story('Become a trader in antiques')
    character.choose_branch('Deal in pretty trinkets')
    character.onwards()

def grind_wines(character):
    """+37 Greyfields 1882 (0.74E)
    scandal on failure
    max persuasive 84 (72% chance)"""
    character.travel(areas.SHUTTERED_PALACE)
    character.begin_story('The Antiquarian Footman')
    character.choose_branch('Offer the fellow a partnership')
    character.onwards()

def grind_clues(character):
    """+30 cryptic clues (0.60E)"""
    character.travel(areas.VEILGARDEN)
    character.begin_story('Correspond with a contact at the Shuttered Palace')
    character.choose_branch('Write a letter')
    character.onwards()

def grind_souls(character):
    """+28 soul (0.56E)
    also has a Shadowy option"""
    character.travel(areas.LADYBONES_ROAD)
    character.begin_story('Track down a Spirifer')
    character.choose_branch('Watch from the rooftops')

def grind_secrets(character):
    """+54 whispered secrets per action (0.54E)"""
    character.travel(areas.VEILGARDEN)
    character.begin_story('The demands of high society')
    character.choose_default_branch()
    character.onwards()