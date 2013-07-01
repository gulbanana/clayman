# alternative grind functions to be used while at the empress' court

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
    if 'Disporting with the servantry' not in character.storylets:
        character.qualities['Fascinating...'] = 0
        return
    character.begin_story('Disporting with the servantry')
    character.choose_branch('Catch the eye of a butler')
    character.onwards()

def fix_wounds(character):
    """-2 to -3 cp"""
    if 'Disporting with the servantry' not in character.storylets:
        character.qualities['Fascinating...'] = 0
        return
    character.begin_story('Disporting with the servantry')
    character.choose_branch('Make overtures to a cook')
    character.onwards()