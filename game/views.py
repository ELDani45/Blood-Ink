# from django.shortcuts import render
# from django.views import View
from django.views.generic import DetailView
from .models import Novel_game
from django.core.paginator import Paginator
# Create your views here.


class Game(DetailView):
    model = Novel_game
    template_name = 'start_game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        scenes_list = self.object.scenes.all()
        paginator = Paginator(scenes_list, 1)
        page_number = self.request.GET.get('page', 1)
        escena_paginada = paginator.get_page(page_number)

        context['scene'] = escena_paginada
        return context
