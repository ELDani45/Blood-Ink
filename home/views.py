from django.shortcuts import render
from novels.models import Description

# Create your views here.


def home(request):
    cards_novels = Description.objects.all()
    print(f"DEBUG: Cantidad de novelas encontradas: {cards_novels.count()}")
    return render(
        request,
        "home.html", {
            'list_novels': cards_novels
        }
    )
