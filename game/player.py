"""The game of player"""
from .general import cards_player, list_penalty_points_row, cards_layout, \
    search_last_cards_layout, cow_penalty_points, penalty_points_player

need_row = 0


def step_player(card, selected_row):
    """The step game of player"""
    global need_row
    condition = check_rule_for_card(card)

    if condition['error'] and len(cards_layout[condition['position']]) != 5:
        cards_layout[condition['position']].append({card: cards_player[card]})
        list_penalty_points_row[condition['position']
                                ][condition['position']][0] += cards_player[card]
        list_penalty_points_row[condition['position']
                                ][condition['position']][1] += 1
        cards_player.pop(card)

    elif check_no_move() or check_card_not_last_one(card):
        if need_row == 0:
            need_row = 1
        else:
            pick_up_row(condition['position'], card, selected_row)
            cards_player.pop(card)
            need_row = 0
    elif len(cards_layout[condition['position']]) == 5:
        pick_up_row(condition['position'], card, selected_row)
        cards_player.pop(card)


def check_rule_for_card(card):
    """Check rule game for card"""
    last_cards = search_last_cards_layout()
    last_card1 = last_cards[0]
    last_card2 = last_cards[1]
    last_card3 = last_cards[2]
    last_card4 = last_cards[3]
    position_cards = {card - last_card1: 0, card -
                      last_card2: 1, card - last_card3: 2, card - last_card4: 3}
    filtered_cards = list(filter(lambda x: x > 0, list(position_cards.keys())))
    if len(filtered_cards) > 0:
        min_value = min(filtered_cards)
        min_dict = position_cards[min_value]
        return {'error': True, 'position': min_dict}
    return {'error': False, 'position': -1000}


def check_card_not_last_one(card):
    """Check card cannot be the last one"""
    list_last_cards = search_last_cards_layout()
    cnt = 0
    for last_card in list_last_cards:
        if last_card - card > 0:
            cnt += 1
    return cnt == len(list_last_cards)


def check_no_move():
    """Check no move"""
    cnt = 0
    for card in cards_player.keys():
        cnt += check_card_not_last_one(card)
    return cnt == len(cards_player)


def pick_up_row(row, card, selected_row):
    """Pick  up row"""
    global penalty_points_player
    if row == -1000:
        row = selected_row
    penalty_points_player += list_penalty_points_row[row][row][0]
    replace_row(row, card)


def replace_row(row, card):
    """Replace row"""
    cards_layout[row].clear()
    cards_layout[row] = [{card: cow_penalty_points(card)}]
    list_penalty_points_row[row][row][0] = cow_penalty_points(card)
    list_penalty_points_row[row][row][1] = 1
