from django.urls import path
from account.views import Profie, Update_profile

app_name = 'account'

urlpatterns = [
    path('profile/', Profie.as_view(), name='profile'),
    path('upload_profile/<int:pk>/', Update_profile.as_view(), name='update')
]
