from django.shortcuts import render
from .models import Description, Genero

# Create your views here."


def description_game(request):
    genero = Genero.objects.all()
    novela = Description.objects.all()
    return render(request, "description.html", {
        "novel": novela, "generos": genero
    })
