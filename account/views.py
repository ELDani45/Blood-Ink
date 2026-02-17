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


class ProfileView(DetailView):
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
    success_url = reverse_lazy('account:profile')
    context_object_name = 'perfil'

    # por defecto django busca el pk que uno le pasa en la url, pero al definir la funcion [ get_object ] = uno puede definir como la plantilla busca el objeto
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_fields'] = FormUserEdit(
                self.request.POST, instance=self.request.user)
        else:
            context['user_fields'] = FormUserEdit(instance=self.request.user)
        return context

    def form_valid(self, form):
        form_user = FormUserEdit(self.request.POST, instance=self.request.user)

        if form_user.is_valid():
            form_user.save()
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

# NOtA : para llamar los campos de del formulario de update
# se hace con la variable predetermianda de django ' form '
# REVISAR EL TEMPLATE =  ' ct_profile.html '
