# alternative grind script to be used while at the empress' court

import _settings
from london import *
from . import common

def grind_secrets(character):
    """+83 whispered secrets per action, and conn:soc
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

character = Character(_settings.AUTH_USER, _settings.AUTH_PASS)
buffer = character.action_cap - 4

while character.actions > buffer:
    if character.qualities['Scandal'] < 7:
        grind_secrets(character)

    elif (character.qualities['Nightmares'] < 7 and
          character.qualities['Wounds'] < 7):
        grind_jade_dog(character)

    else:
        grind_honey(character)
        #or: grind_jade_youth(character)