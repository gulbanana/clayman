from common import *

def main():
    with_character(lambda c: with_buffer(c, ai))

    def ai(character):
        # keep 1000 of this around for the presumptuous little oppportunity
        if (character.persuasive < 85
            and character.items['Greyfields 1882'] < 1000
            and character.qualities['Scandal'] < 7):
            grind.greyfields_1882(character)

        # save up for lodgings
        elif character.items['Whispered Secret'] < 80000:
            grind.whispered_secrets(character)

        elif character.items['Soul'] < 40000:
            grind.souls(character)

        # get money with risk of scandal
        elif character.qualities['Scandal'] < 7:
            grind.jade_watchful(character)

        # get money with no risk
        else:
            grind.cryptic_clues(character)