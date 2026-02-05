# from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
# Create your views here.


class Profie(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
