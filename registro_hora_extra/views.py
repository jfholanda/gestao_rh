from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


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

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs