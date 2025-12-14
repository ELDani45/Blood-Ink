from django.urls import path  #
from . import views


app_name = "login"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signout/", views.signout, name="signout"),
    path("signin/", views.signin, name="signin"),
]
