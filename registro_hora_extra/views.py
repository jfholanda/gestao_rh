from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views import View
from django.urls import reverse_lazy
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.http import HttpResponse
import json


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self) -> QuerySet[Any]:
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset
    
class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']

    # def get_form_kwargs(self):
    #     kwargs = super(HoraExtraCreate, self).get_form_kwargs()
    #     kwargs.update({'user': self.request.user})
    #     return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps({
            'mensagem': 'Requisicao Executada', 
            'horas': float(funcionario.total_horas_extra)
        })
        return HttpResponse(response, content_type='application/json')