from django.urls import path
from . import views

urlpatterns = [path("description/", views.description_game, name="description")]
