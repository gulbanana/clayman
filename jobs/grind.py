import _settings
from london import *
from .common import *

def grind_wines(character):
    """+37 Greyfields 1882 per action (0.74E)
    max persuasive 84 (72% chance)"""
    character.travel(areas.SHUTTERED_PALACE)
    character.begin_story('The Antiquarian Footman')
    character.choose_branch('Offer the fellow a partnership')
    character.onwards()

def grind_secrets(character):
    """+54 whispered secrets per action (0.54E)"""
    character.travel(areas.VEILGARDEN)
    character.begin_story('The demands of high society')
    character.choose_branch('Attend an event')
    character.onwards()

def grind_clues(character):
    """+30 cryptic clues per action(0.60E)"""
    character.travel(areas.VEILGARDEN)
    character.begin_story('Correspond with a contact at the Shuttered Palace')
    character.choose_branch('Write a letter')
    character.onwards()

character = Character(_settings.AUTH_USER, _settings.AUTH_PASS)

buffer = character.action_cap - 4
while character.actions > buffer:
    if character.menaces['Scandal'] < 7:
        grind_wines(character)
    elif character.items['Whispered Secret'] < 80000:
        grind_secrets(character)
    else:
        grind_clues(character)