from django.shortcuts import render
import random
import time


# Create your views here.


def home(request):
    return render(request, 'game/home.html')


def play_game(request, player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        result = "Tie 🟰"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You win 🏆'
    else:
        result = 'You lose 😔'
    time.sleep(2)
    return render(request, 'game/play_game.html',
                  {'player_choice': player_choice, 'computer_choice': computer_choice, 'result': result})
