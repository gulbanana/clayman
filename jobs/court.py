# alternative grind script to be used while at the empress' court

import _settings
from london import *

def grind_secrets(character):
    """+83 whispered secrets per action, and conn:soc
    fail: -fascinating"""
    character.begin_story('Attend to matters of romance')
    character.choose_branch('Attend courtly functions')
    character.onwards()

def grind_clues(character):
    """+44 cryptic clues per action, and fascinating
    fail: scandal"""
    character.begin_story('Attend to matters of romance')
    character.choose_branch('Take a stroll in the gardens')
    character.onwards()

def grind_influence(character):
    """+18 stolen correspondence per action, and conn:soc
    fail: scandal"""
    character.begin_story('Attend to matters of romance')
    character.choose_branch('Write a letter')
    character.onwards()

def grind_jade_dog(character):
    """+88 jade per action, and nightmares
    fail: nightmares & wounds"""
    character.begin_story("Make friends with the Empress' dog")
    character.choose_branch('Give the puppy a biscuit')
    character.onwards()

def grind_jade_youth(character):
    """+91 jade per action, and +hedonist
    fail: -hedonist
    higher difficulty than dog"""
    character.begin_story('The Corruption of Youth')
    character.choose_branch('The seduction of music')
    character.onwards()

def grind_honey(character):
    """+45 honey per action, and +hedonist
    fail: -hedonist"""
    character.begin_story('The Corruption of Youth')
    character.choose_branch('Join a picnic expedition')
    character.onwards()

def fix_scandal(character):
    """-2 cp"""
    character.begin_story('Disporting with the servantry')
    character.choose_branch('Catch the eye of a butler')
    character.onwards()

def fix_wounds(character):
    """-2 to -3 cp"""
    character.begin_story('Disporting with the servantry')
    character.choose_branch('Make overtures to a cook')
    character.onwards()

def main():
    character = Character(_settings.AUTH_USER, _settings.AUTH_PASS)
    buffer = character.action_cap - 4

    # get to court
    character.travel(areas.EMPRESS_COURT) # doesn't actually work, just refreshes storylets

    # be hella social
    while character.actions > buffer:
        if (character.qualities['Scandal'] > 5 and
            character.qualities['Fascinating...'] >= 4):
            fix_scandal(character)

        elif (character.qualities['Wounds'] > 5 and
            character.qualities['Fascinating...'] >= 5):
            fix_wounds(character)

        elif character.items['Whispered Secret'] < 80000:
            grind_secrets(character)

        elif character.qualities['Scandal'] < 7:
            grind_clues(character)

        elif (character.qualities['Nightmares'] < 7 and
              character.qualities['Wounds'] < 7):
            grind_jade_dog(character)

        else:
            grind_honey(character)
            #or: grind_jade_youth(character)