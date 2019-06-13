from django.db import models


class Prescricao(models.Model):
    nome_medico = models.CharField(max_length=250)
    data_emissao = models.CharField(max_length=25)
    texto_receita = models.CharField(max_length=5000)

    def __str__(self):
        return self.data_emissao + ' - ' + self.nome_medico


class Remedio(models.Model):
    prescricao = models.ForeignKey(Prescricao)
    nome_remedio = models.CharField(max_length=250)
    texto_remedio = models.CharField(max_length=10000)
