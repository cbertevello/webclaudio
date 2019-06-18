from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.views import generic
from django.views.generic import View
from .models import Prescricao
from .forms import UserForm

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


class UserFormView(View):
    form_class = UserForm
    template_name = 'receitas/registration_form.html'
    # mostra um formulário "em branco"
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # processando dados do formulário
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # dados limpos (normalizados)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #retorna objetos "User" (se os dados estiverem corretos)
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('receitas:index')

        return render(request, self.template_name, {'form': form})


