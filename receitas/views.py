from django.shortcuts import render, get_object_or_404
from .models import Prescricao


def index(request):
    all_prescricoes = Prescricao.objects.all()
    return render(request, 'receitas/index.html', {'all_prescricoes': all_prescricoes})

def detail(request, prescricao_id):
    prescricao = get_object_or_404(Prescricao, pk=prescricao_id)
    return render(request, 'receitas/detail.html', {'prescricao': prescricao})
