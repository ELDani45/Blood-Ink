from django.shortcuts import render
from .models import Description, Genero

# Create your views here."


def description_game(request):
    novela = Description.objects.all()
    return render(request, "description.html", {
        "novel": novela
    })
