# from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView

from account.forms import Form_edit_profile
from account.models import Profile
from login.forms import SingUp
from novels.models import Description

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
    form_class = Form_edit_profile
    template_name = 'act_profile.html'
    # NOTA: cambiar la redireccion del usuarrio [ de home a = profile]
    success_url = 'home:home'
    context_object_name = 'perfil'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_fields'] = SingUp()
        return context

# NOtA : para llamar los campos de del formulario de update
# se hace con la variable predetermianda de django ' form '
# REVISAR EL TEMPLATE =  ' ct_profile.html '
