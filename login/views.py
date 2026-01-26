# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from login.forms import SignIn, SingUp
from django.views.generic import CreateView
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin tal vez se utilize en futuras ocaciones, esta vista sirve para restringir ñas vistas al que un usario no autenticado puede ver


# Create your views here.


class Registrate(CreateView):
    form_class = SingUp
    template_name = 'login/login.html'
    success_url = reverse_lazy('home:home')


def signout(request):
    logout(request)
    return redirect("home:home")


def signin(request):

    if request.method == "GET":
        return render(request, "login/signin.html", {"form": SignIn})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login/signin.html",
                {
                    "form": SignIn,
                    "message": "Usuario o contraseña incorrecto",
                },
            )
        else:
            auth_login(request, user)
            return redirect("home:home")
