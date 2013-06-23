import _settings
from london import *

character = Character(_settings.AUTH_USER, _settings.AUTH_PASS)
character.travel(areas.LODGINGS)
character.begin_story('Write Letters')
character.perhaps_not()