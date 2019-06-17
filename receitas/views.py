from django.views import generic
from .models import Prescricao

class IndexView(generic.ListView):
    template_name = 'receitas/index.html'
    context_object_name = 'all_prescricoes'

    def get_queryset(self):
        return Prescricao.objects.all()

class DetailView(generic.DetailView):
    model = Prescricao
    template_name = 'receitas/detail.html'
