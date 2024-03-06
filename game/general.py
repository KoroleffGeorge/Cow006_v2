"""General functions and parametrize of game"""
import math
import random


card_deck = []
cards_computer = {}
cards_player = {}
cards_layout = []
set_of_player_cards = set()
penalty_points_player = 0
penalty_points_computer = 0
list_penalty_points_row = [{0: [0, 0]}, {1: [0, 0]}, {2: [0, 0]}, {3: [0, 0]}]


def cow_penalty_points(number):
    """Count penalty points"""
    units = math.trunc(number % 10)
    tens = math.trunc(number / 10)
    if units == 5 & tens == 5:
        return 7
    if units == tens:
        return 5
    if units == 0:
        return 3
    if units == 5:
        return 2
    return 1


def generation_card_deck():
    """Generation card deck"""
    for i in range(1, 105):
        card_deck.append(i)


def dealing_cards():
    """Dealing cards"""
    random.shuffle(card_deck)
    for i in range(1, 21):
        if i % 2 == 0:
            cards_player[card_deck[i]] = cow_penalty_points(card_deck[i])
        else:
            cards_computer[card_deck[i]] = cow_penalty_points(card_deck[i])
    cards_layout.append([{card_deck[21]: cow_penalty_points(card_deck[21])}])
    list_penalty_points_row[0][0][0] = cow_penalty_points(card_deck[21])
    cards_layout.append([{card_deck[22]: cow_penalty_points(card_deck[22])}])
    list_penalty_points_row[1][1][0] = cow_penalty_points(card_deck[22])
    cards_layout.append([{card_deck[23]: cow_penalty_points(card_deck[23])}])
    list_penalty_points_row[2][2][0] = cow_penalty_points(card_deck[23])
    cards_layout.append([{card_deck[24]: cow_penalty_points(card_deck[24])}])
    list_penalty_points_row[3][3][0] = cow_penalty_points(card_deck[24])
    list_penalty_points_row[0][0][1] = list_penalty_points_row[1][1][1] = \
        list_penalty_points_row[2][2][1] = list_penalty_points_row[3][3][1] = 1


def search_last_cards_layout():
    """Search last cards layout"""
    last_card1 = list(cards_layout[0][len(cards_layout[0]) - 1].keys())[0]
    last_card2 = list(cards_layout[1][len(cards_layout[1]) - 1].keys())[0]
    last_card3 = list(cards_layout[2][len(cards_layout[2]) - 1].keys())[0]
    last_card4 = list(cards_layout[3][len(cards_layout[3]) - 1].keys())[0]
    return [last_card1, last_card2, last_card3, last_card4]


def check_end_game():
    """Check end game"""
    return len(cards_player) == 0 and len(cards_computer) == 0
