from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from departamentos.models import Departamento
from django.contrib.auth.models import User
from unidecode import unidecode


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset
    
class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def get_form(self, form_class=None): #Mostrando apenas os departamentos atrelados à empresa do funcionário
        form = super().get_form(form_class)
        empresa = self.object.empresa
        form.fields['departamentos'].queryset = Departamento.objects.filter(empresa=empresa)

        return form

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def get_form(self, form_class=None): #Mostrando apenas os departamentos atrelados à empresa do funcionário
        form = super().get_form(form_class)
        empresa = self.object.empresa
        form.fields['departamentos'].queryset = Departamento.objects.filter(empresa=empresa)

        return form

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        try:
            username = unidecode(funcionario.nome.split()[0]) + unidecode(funcionario.nome.split()[1]).lower()
        except IndexError:
             username = unidecode(funcionario.nome.split()[0].lower())
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)


