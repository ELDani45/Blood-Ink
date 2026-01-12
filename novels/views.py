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
        form = Makenovel(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = Makenovel()
        return render(request, "make_novel.html", {
            'form_Novel': form
        })


def update_description(request, id_description=None) -> object:
    description = Description.objects.get(id=id_description)
    if request.method == "GET":
        form_novel = Makenovel(instance=description)
        # Renderizar page
        return render(request, "update_description.html", {
            "form_novel": form_novel,
            "description": description
        })

    if request.method == "POST":
        form_novel = Makenovel(instance=description, data=request.POST)
        if form_novel.is_valid():
            form_novel.save()
            return redirect("home:home")
        else:
            form_novel = Makenovel(instance=description, data=request.POST)
        return render(request, "update_description.html", {
            "form_novel": form_novel,
            "description": description
        })


def prologue(request, id):
    prologo = Description.objects.get(id=id)
    return render(request, "prologo.html", {
        "prologue": prologo
    })


def novels_delete(request, id=None):
    novela = get_object_or_404(Description, id=id)
    novela.delete()
    return redirect("home:home")
