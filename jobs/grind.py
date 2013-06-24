import _settings
from london import *
from .common import *

character = Character(_settings.AUTH_USER, _settings.AUTH_PASS)
buffer = character.action_cap - 4

while character.actions > buffer:
    if character.menaces['Scandal'] < 7 and character.items['Greyfields 1882'] < 1000:
        grind_wines(character)
    elif character.items['Whispered Secret'] < 80000:
        grind_secrets(character)
    elif character.menaces['Scandal'] < 7:
        grind_jade(character)
    else:
        grind_clues(character)