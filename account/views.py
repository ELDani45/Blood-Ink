# from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User
from novels.models import Description
from account.models import Profile

# from django.shortcuts import get_object_or_404
# Create your views here.


class Profie(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description'] = Description.objects.filter(author=self.object)
        return context


class Update_profile(UpdateView):
    model = Profile
    fields = ['user', 'image_profile', 'social_network', 'about_me']
    template_name = 'act_profile.html'
    success_url = 'home:home'
    context_object_name = 'perfil'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_fields'] = User.objects.all()
        return context
