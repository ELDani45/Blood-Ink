from django.urls import path
from . import views


app_name = "novels"

urlpatterns = [  # Aqui <int { Es el tipo de dato que el servidor va a recibir } : pk { pk es la instancia que va a recibir, en este caso va a recibir un ID }
    path("novels/delete/<int:id>/", views.novels_delete, name="delete"),
    path("description/<int:id>/", views.description_game, name="description"),
    path("novels/update/<int:id_description>/",
         views.update_description, name="update"),
    path("novels/vista/prologue/<int:id>/", views.prologue, name="prologue"),
    path("make_novel", views.hacer_novel, name="making_novel"),
    path('description/like/<int:id>/',
         views.like_view, name='like')
]
