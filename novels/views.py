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
    # Caso 1: El usuario envía el formulario (POST)
    if request.method == 'POST':
        form = Makenovel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Asegúrate de que 'home:home' exista en tus URLs
            return redirect('home:home')
        # Si NO es válido, NO creamos un formulario nuevo.
        # Usamos el 'form' actual que ya tiene los errores y los datos.

    # Caso 2: El usuario entra por primera vez (GET)
    else:
        form = Makenovel()  # <--- IMPORTANTE: Usar paréntesis () para crear instancia

    # Un solo render al final para ambos casos (limpio y seguro)
    return render(request, "make_novel.html", {
        'form_Novel': form
    })
