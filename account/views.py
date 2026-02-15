# from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from account.forms import Form_edit_profile
from account.models import Profile
from account.forms import FormUserEdit
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
        # Traemos los datos del profile del usuaorio
        context['user_profile'] = Profile.objects.get(user=self.request.user)
        return context


class Update_profile(UpdateView):
    model = Profile
    form_class = Form_edit_profile
    template_name = 'act_profile.html'
    # NOTA: cambiar la redireccion del usuarrio [ de home a = profile]
    success_url = reverse_lazy('home:home')
    context_object_name = 'perfil'

    # por defecto django busca el pk que uno le pasa en la url, pero al definir la funcion [ get_object ] = uno puede definir como la plantilla busca el objeto
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            # Si hay un error, mantenemos lo que el usuario escribió
            context['user_fields'] = FormUserEdit(
                self.request.POST, instance=self.request.user)
        else:
            # Si es la primera vez que entra, cargamos sus datos actuales
            context['user_fields'] = FormUserEdit(instance=self.request.user)
        return context

    def form_valid(self, form):
        # 1. Cargamos el formulario con los datos que vienen del HTML (POST)
        # y lo vinculamos al usuario actual (instance)
        form_user = FormUserEdit(self.request.POST, instance=self.request.user)

        if form_user.is_valid():
            form_user.save()  # <--- Esto guarda en la tabla 'auth_user'
            form.save()       # <--- Esto guarda en la tabla 'Profile'
            return super().form_valid(form)
        else:
            # Si el usuario es inválido (ej. email duplicado), vuelve al form con errores
            return self.form_invalid(form)

# NOtA : para llamar los campos de del formulario de update
# se hace con la variable predetermianda de django ' form '
# REVISAR EL TEMPLATE =  ' ct_profile.html '
