from django.urls import path
from account.views import Update_profile, ProfileView
from novels.views import description_game

app_name = 'account'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('upload_profile/<int:pk>/', Update_profile.as_view(), name='update'),
    path('novels/description/<int:id>/',
         description_game, name='description_novel')
]
