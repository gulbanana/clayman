from common import *

def main():
    with_character(lambda c: with_buffer(c, ai))

    def ai(character):
        if (character.persuasive < 85
            and character.items['Greyfields 1882'] < 1000
            and character.qualities['Scandal'] < 7):
            grind.grind_wines(character)

        elif character.items['Whispered Secret'] < 80000:
            grind.grind_secrets(character)

        elif character.qualities['Scandal'] < 7:
            grind.grind_jade(character)

        else:
            grind.grind_clues(character)