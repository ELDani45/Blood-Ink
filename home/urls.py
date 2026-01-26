from django.urls import path
from home.views import Home
# from . import views ) = se utiliza en el caso de que se trabaje con vistas en funciojnes

app_name = "home"

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
