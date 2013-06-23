import _settings
from london import *
from .common import *

character = Gentleperson(_settings.AUTH_USER, _settings.AUTH_PASS)

buffer = character.action_cap - 2

print('actions before: ' +str(character.actions))
grind_wines(character)
print('actions after: ' +str(character.actions))