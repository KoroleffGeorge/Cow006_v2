"""The main function of the game"""
from .computer import step_computer
from .general import generation_card_deck, dealing_cards, check_end_game
from .player import step_player


def gaming(step_game, selected_card, selected_row):
    """The logic of the game"""
    if step_game == 1:
        generation_card_deck()
        dealing_cards()
    if step_game < 21:
        if check_end_game():
            exit()
        if step_game % 2 == 0:
            step_player(selected_card, selected_row)
        else:
            step_computer()
