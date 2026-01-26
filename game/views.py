from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
# Create your views here.


class Game(DetailView):
    model = 'aun_no'
