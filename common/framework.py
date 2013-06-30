import _settings
from london import *

def with_character(f):
    character = Character(_settings.AUTH_USER, _settings.AUTH_PASS)
    f(character)

def with_buffer(character, f):
    buffer = character.action_cap - 4
    while character.actions > buffer:
        f(character)