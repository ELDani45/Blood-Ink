# from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from novels.models import Description

# Create your views here.

# CLASES GENERICAS:
# DetailView = Para mostrar los detalles de un unico objeto


class Home(ListView):
    model = Description
    template_name = 'home.html'
    context_object_name = 'list_novels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #  definimos el nombre en eñ que se pasaran los daros al template( denntro de los corchetes [] )
        context['list_novels'] = Description.objects.all()
        return context


class AboutUs(TemplateView):
    template_name = 'about_us.html'
