from django.urls import path
from . import views


app_name = "novels"

urlpatterns = [  # Aqui <int { Es el tipo de dato que el servidor va a recibir } : pk { pk es la instancia que va a recibir, en este caso va a recibir un ID }
    path("description/<int:id>/", views.description_game, name="description"),
    path("update/<int:id>/", views.update_description, name="update"),
    path("make_novel", views.hacer_novel, name="making_novel")
]
