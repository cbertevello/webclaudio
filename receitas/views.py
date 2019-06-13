from django.http import HttpResponse
from .models import Prescricao


def index(request):
    all_prescricaos = Prescricao.objects.all()
    html = ''
    for prescricao in all_prescricaos:
        url = '/receitas/' + str(prescricao.id) + '/'
        html += '<a href="' + url + '">' + prescricao.nome_medico + ', de: ' + prescricao.data_emissao + '</a><br>'
    return HttpResponse(html)


def detail(request, prescricao_id):
    return HttpResponse("<h2>Detalhes da Prescrição id: "+str(prescricao_id) + "</h2>")
