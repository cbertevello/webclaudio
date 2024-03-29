from django.db import models
from django.core.urlresolvers import reverse



#class Song(models.Model):
class Remedio(models.Model):
    nome_remedio = models.CharField(max_length=250, default='()_Sem Remédio')
    texto_remedio = models.TextField()
    #is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.nome_remedio

#class Album(models.Model):
class Prescricao(models.Model):
    nome_medico = models.CharField(max_length=250)
    data_ano_mes_dia = models.CharField(max_length=8)
    data_mes_texto = models.CharField(max_length=25)
    texto_receita = models.TextField()

    # ----------------------------------------------------------------

    remedio1 = models.ForeignKey(Remedio, related_name="remedio1s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio1 is None:  # Set default reference
            self.remedio1 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    remedio2 = models.ForeignKey(Remedio, related_name="remedio2s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio2 is None:  # Set default reference
            self.remedio2 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    remedio3 = models.ForeignKey(Remedio, related_name="remedio3s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio3 is None:  # Set default reference
            self.remedio3 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    remedio4 = models.ForeignKey(Remedio, related_name="remedio4s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio4 is None:  # Set default reference
            self.remedio4 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    remedio5 = models.ForeignKey(Remedio, related_name="remedio5s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio5 is None:  # Set default reference
            self.remedio5 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    remedio6 = models.ForeignKey(Remedio, related_name="remedio6s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio6 is None:  # Set default reference
            self.remedio6 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    remedio7 = models.ForeignKey(Remedio, related_name="remedio7s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio7 is None:  # Set default reference
            self.remedio7 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    remedio8 = models.ForeignKey(Remedio, related_name="remedio8s", null=True)

    def save(self, *args, **kwargs):
        if self.remedio8 is None:  # Set default reference
            self.remedio8 = Remedio.objects.get(id=1)
        super(Prescricao, self).save(*args, **kwargs)

    # ----------------------------------------------------------------

    def get_absolute_url(self):
        return reverse('receitas:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.data_mes_texto + ' - ' + self.nome_medico
