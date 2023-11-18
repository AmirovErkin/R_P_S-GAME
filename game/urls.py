from django.urls import path
from .views import home, play_game

urlpatterns = [
    path('', home, name='home'),
    path('play/<str:player_choice>/', play_game, name='play_game'),
]
