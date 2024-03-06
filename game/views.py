"""App views"""
from django.shortcuts import render, redirect
from .game_overall import gaming
from .general import cards_computer, cards_player, cards_layout
from . import player, computer

step = 0
messageWas = 0
card = 0
row = -1


def index(request):
    """Generation start page"""
    return render(request, 'index.html')


def play(request):
    """Make move on the game"""
    global step
    global messageWas
    global card
    global row
    step += 1

    if (step < 21):
        if player.need_row == 1:
            step -= 1

        if (step % 2 != 0):
            print(request.POST, "29")
            gaming(step, 0, 0)
            context = {
                'cards_computer': cards_computer,
                'cards_player': cards_player,
                'cards_layout': cards_layout,
                'penalty_points_computer':  computer.penalty_points_computer,
                'penalty_points_player': player.penalty_points_player,
            }
            return render(request, 'game.html', context)
        else:
            print(request.POST)
            row = -1

            if player.need_row == 0 and 'selected_card' in request.POST:
                card = int(request.POST.get('selected_card'))
                gaming(step, card, 0)

            if player.need_row == 1 and messageWas == 0:
                messageWas = 1
                card = int(request.POST.get('selected_card'))
                context = {
                    'cards_computer': cards_computer,
                    'cards_player': cards_player,
                    'cards_layout': cards_layout,
                    'penalty_points_computer':  computer.penalty_points_computer,
                    'penalty_points_player': player.penalty_points_player,
                    'message': "Need row"
                }

                return render(request, 'game.html', context)

            if player.need_row == 1 and messageWas == 1:
                messageWas = 0
                row = int(request.POST.get('selected_row')) - 1
                gaming(step, card, row)

            return redirect('/play')
    else:
        if computer.penalty_points_computer < player.penalty_points_player:
            message = "Game over! Computer win"
        else:
            message = "Game over! Player win"
        context = {
                    'cards_computer': cards_computer,
                    'cards_player': cards_player,
                    'cards_layout': cards_layout,
                    'penalty_points_computer':  computer.penalty_points_computer,
                    'penalty_points_player': player.penalty_points_player,
                    'message': message
                }
        return render(request, 'game.html', context)
