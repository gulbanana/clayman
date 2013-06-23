import _settings
from london import *

character = Character(_settings.AUTH_USER, _settings.AUTH_PASS)

character.use_item('Soul')
character.choose_branch('Deal with the Infernal Sommelier')