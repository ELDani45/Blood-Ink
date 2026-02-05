from django.urls import path
from account.views import Profie

app_name = 'account'

urlpatterns = [
    path('profile/', Profie.as_view(), name='profile')
]
