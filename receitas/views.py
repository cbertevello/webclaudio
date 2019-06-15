from django.http import Http404
from django.shortcuts import render
from .models import Prescricao


def index(request):
    all_prescricoes = Prescricao.objects.all()
    return render(request, 'receitas/index.html', {'all_prescricoes': all_prescricoes})

def detail(request, prescricao_id):
    try:
        prescricao = Prescricao.objects.get(pk=prescricao_id)
    except Prescricao.DoesNotExist:
        raise Http404("NÃO EXISTE ESTA PRESCRIÇÃO!")
    return render(request, 'receitas/detail.html', {'prescricao': prescricao})
