# to be used while at the empress' court

import _settings
from london import *
from common import *

def init(character):
    character.travel(areas.EMPRESS_COURT) # doesn't actually work, just refreshes storylets
    with_buffer(character, ai)

def ai(character):
    if (character.qualities['Scandal'] > 5 and
        character.qualities['Fascinating...'] >= 4):
        court.fix_scandal(character)

    elif (character.qualities['Wounds'] > 5 and
        character.qualities['Fascinating...'] >= 5):
        court.fix_wounds(character)

    elif character.items['Whispered Secret'] < 80000:
        court.grind_secrets(character)

    elif character.qualities['Scandal'] < 7:
        court.grind_clues(character)

    elif (character.qualities['Nightmares'] < 7 and
          character.qualities['Wounds'] < 7):
        court.grind_jade_dog(character)

    else:
        court.grind_honey(character)
        #or: grind_jade_youth(character)

def main():
    with_character(init)