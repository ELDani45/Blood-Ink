from django.shortcuts import render, redirect, get_object_or_404
from .models import Description
from novels.forms import Makenovel

# Create your views here."


def description_game(request, id=None):
    description = get_object_or_404(Description, id=id)
    return render(request, "description.html", {
        "novela": description
    })


def hacer_novel(request):
    if request.method == 'POST':
        form = Makenovel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = Makenovel()
        return render(request, "make_novel.html", {
            'form_Novel': form
        })
