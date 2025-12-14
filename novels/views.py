from django.shortcuts import render

# Create your views here.


def description_game(request):
    render(request, "description")
