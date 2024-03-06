"""The game of computer"""
from operator import itemgetter

from .general import cards_computer, cards_layout, list_penalty_points_row, \
    search_last_cards_layout, cow_penalty_points, penalty_points_computer


def step_computer():
    """The step game of computer"""
    preliminary_calculations()


# расстановка карт ии в выгодном для него порядке
def preliminary_calculations():
    """Preliminary calculations before the move"""
    order_cards = sorted(search_position(), key=itemgetter(0, 1, 3))
    status = check_move_computer_available(
        order_cards[0][0], order_cards[0][1])
    choice_row = {}
    choice_card = {}
    if status == 0:
        edit_card = selection_minimum_card(
            status, [{lst[3]: lst[2]} for lst in order_cards if lst[1] < 5])
        choice_card = {
            list(
                edit_card.keys())[0]: list(
                edit_card.values())[0][0]}
        choice_row = list(edit_card.values())[0][1]
    if status == 1:
        choice_row = list(
            sorted(
                list_penalty_points_row,
                key=lambda x: list(
                    x.values())[0])[0].keys())[0]
        choice_card = selection_minimum_card(status, [])
    if status == 2:
        info = sort_on_status(sorted(order_cards, key=lambda x: (x[4], x[3])))
        choice_row = info[0]
        choice_card = info[1]
    make_decision(choice_card, choice_row, status)


def sort_on_status(order_cards):
    """Selection of a possible row and card"""
    row = -1
    card = {}
    for list_card in order_cards:
        if list_card[2] >= 0:
            row = list_card[2]
            card = {list_card[3]: cow_penalty_points(list_card[3])}
            break
    return [row, card]


def make_decision(choice_card, choice_row, status):
    """Making a computer move"""
    global penalty_points_computer
    if status == 0:
        list_penalty_points_row[choice_row][choice_row][0] += list(choice_card.values())[0]
        list_penalty_points_row[choice_row][choice_row][1] += 1
        cards_layout[choice_row].append(choice_card)
    if status == 1:
        penalty_points_computer += list_penalty_points_row[choice_row][choice_row][0]
        list_penalty_points_row[choice_row][choice_row][0] = list(choice_card.values())[0]
        list_penalty_points_row[choice_row][choice_row][1] = 1
        cards_layout[choice_row] = [choice_card]
    if status == 2:
        penalty_points_computer += list_penalty_points_row[choice_row][choice_row][0]
        list_penalty_points_row[choice_row][choice_row][0] = list(choice_card.values())[0]
        list_penalty_points_row[choice_row][choice_row][1] = 1
        cards_layout[choice_row] = [choice_card]
    cards_computer.pop(list(choice_card.keys())[0])


def selection_minimum_card(status, order_cards):
    """Selection minimum card"""
    result = {}
    if status == 1:
        num = min(cards_computer.keys())
        result = {num: cards_computer.get(num)}
    if status == 2:
        num = min(order_cards)
        result = {num: cow_penalty_points(num)}
    if status == 0:
        num = min(order_cards, key=lambda x: next(iter(x)))
        result = {
            list(
                num.keys())[0]: [
                cow_penalty_points(
                    list(
                        num.keys())[0]), list(
                    num.values())[0]]}
    return result


def check_move_computer_available(diff, pos):
    """Analysis of the computer's progress scenario"""
    result = 0
    if diff == 1000:
        result = 1
    if pos == 5:
        result = 2
    return result


def search_position():
    """Search position for card"""
    mass = []
    last_cards = search_last_cards_layout()
    for i in cards_computer.keys():
        pos = -1
        diff = 1000
        for j in range(len(last_cards)):
            if (i - last_cards[j] < diff) and (i - last_cards[j] > 0):
                diff = i - last_cards[j]
                pos = j
        if pos == -1:
            mass.append([diff, 10, pos, i, 1000, 1000])
        else:
            mass.append([diff, len(cards_layout[pos]), pos, i,
                        list_penalty_points_row[pos][pos][0], last_cards[pos]])
    return mass
