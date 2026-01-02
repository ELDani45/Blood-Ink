from django.urls import path
from . import views


app_name = "novels"

urlpatterns = [
    path("description/", views.description_game, name="description"),
    path("make_novel", views.hacer_novel, name="making_novel")
]
