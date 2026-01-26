from django.urls import path
from game.views import Game

app_name = 'game'

urlpatterns = [
    path('game/', Game.as_view(), name='game')
]
