from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Prescricao

class IndexView(generic.ListView):
    template_name = 'receitas/index.html'
    context_object_name = 'all_prescricoes'

    def get_queryset(self):
        return Prescricao.objects.all()

class DetailView(generic.DetailView):
    model = Prescricao
    template_name = 'receitas/detail.html'

class AlbumCreate(CreateView):
    model = Prescricao
    fields = ['nome_medico', 'data_ano_mes_dia', 'data_mes_texto', 'texto_receita']
