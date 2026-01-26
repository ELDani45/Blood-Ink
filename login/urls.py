from django.urls import path  #
from login.views import Registrate
from . import views


app_name = "login"

urlpatterns = [
    path("login/", Registrate.as_view(), name="login"),
    path("signout/", views.signout, name="signout"),
    path("signin/", views.signin, name="signin"),
]
