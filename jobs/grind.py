from common import *

def main():
    with_character(lambda c: with_buffer(c, ai))

    def ai(character):
        # keep 1000 of this around for the presumptuous little oppportunity
        if (character.persuasive < 85
            and character.items['Greyfields 1882'] < 1000
            and character.qualities['Scandal'] < 7):
            grind.palace_wines(character)

        # save up for a lodgings
        elif character.items['Whispered Secret'] < 80000:
            grind.veilgarden_secrets(character)

        # get money with risk of scandal
        elif character.qualities['Scandal'] < 7:
            grind.palace_jade(character)

        # get money with no risk
        else:
            grind.veilgarden_clues(character)