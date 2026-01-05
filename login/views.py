# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from login.forms import SignIn, SingUp

# from django.http import HttpResponse

# Create your views here.


def login(request):
    if request.method == 'GET':
        form = SingUp()
        return render(request, "login/login.html", {"form": form})

    if request.method == "POST":
        form = SingUp(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home:home")
        else:
            return render(request, "login/login.html", {"form": form})
    else:
        form = SingUp()
        return render(request, "login/login.html", {"form": form})


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
