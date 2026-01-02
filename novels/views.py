from django.shortcuts import render, redirect
from .models import Description
from novels.forms import Makenovel

# Create your views here."


def description_game(request):
    novela = Description.objects.all()
    return render(request, "description.html", {
        "novel": novela
    })


def hacer_novel(request):
    if request.method == 'GET':
        return render(request, "make_novel.html", {
            'form_Novel': Makenovel
        })

    if request.method == 'POST':
        form = Makenovel(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        else:
            form = Makenovel(data=request.POST)
            return render(request, "make_novel.html", {
                'form_Novel': Makenovel})
