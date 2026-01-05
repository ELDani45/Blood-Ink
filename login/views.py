from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as auth_login
from login.forms import SignIn, SingUp

# from django.http import HttpResponse

# Create your views here.


def login(request):

    if request.method == "GET":
        return render(request, "login/login.html", {"form": SingUp})

    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )

                auth_login(request, user)
                return redirect(
                    "home:home",
                    {
                        "form": SingUp,
                        "message": "Usuario creado sactifastoriamente",
                    },
                )

            except ImportError:
                return render(
                    request,
                    "login/login.html",
                    {"form": SingUp, "message": "El usuario ya existe"},
                )

        else:
            return render(
                request,
                "login/login.html",
                {"form": SingUp, "message": "Las contraselas no coinciden"},
            )


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
