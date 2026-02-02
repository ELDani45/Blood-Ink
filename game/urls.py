from django.urls import path
from game.views import Game

app_name = 'game'

urlpatterns = [
    path('game/<int:pk>/', Game.as_view(), name='game')
]
