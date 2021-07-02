from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import RubroGasto,RubroVenta,Subrubro,Umedida
from .forms import RubroGastoForm,RubroVentaForm,SubRubroGastoForm,UmedidaForm

class RubroGastoList(ListView):
    model = RubroGasto

class RubroGastoCrear(CreateView):
    model = RubroGasto
    form_class = RubroGastoForm
    success_url = reverse_lazy('economico:rubro-gasto')

class RubroGastoEdit(UpdateView):
    model = RubroGasto
    form_class = RubroGastoForm
    success_url = reverse_lazy('economico:rubro-gasto')

class RubroGastoDelete(DeleteView):
    model = RubroGasto
    form_class = RubroGastoForm
    success_url = reverse_lazy('economico:rubro-gasto')

class RubroVentaList(ListView):
    model = RubroVenta

class RubroVentaCrear(CreateView):
    model = RubroVenta
    form_class = RubroVentaForm
    success_url = reverse_lazy('economico:rubro-venta')

class RubroVentaEdit(UpdateView):
    model = RubroVenta
    form_class = RubroVentaForm
    success_url = reverse_lazy('economico:rubro-venta')

class RubroVentaDelete(DeleteView):
    model = RubroVenta
    form_class = RubroVentaForm
    success_url = reverse_lazy('economico:rubro-venta') 

class SubrubroGastoList(ListView):
    model = Subrubro
    template_name = 'economico/subrubro_list.html'

class SubrubroGastoCrear(CreateView):
    model = Subrubro
    form_class = SubRubroGastoForm
    success_url = reverse_lazy('economico:subrubro-gasto')

class SubrubroGastoEdit(UpdateView):
    model = Subrubro
    form_class = SubRubroGastoForm
    success_url = reverse_lazy('economico:subrubro-gasto')

class SubrubroGastoDelete(DeleteView):
    model = Subrubro
    form_class = SubRubroGastoForm
    success_url = reverse_lazy('economico:subrubro-gasto') 

class UmedidaList(ListView):
    model = Umedida

class UmedidaCrear(CreateView):
    model = Umedida
    form_class = UmedidaForm
    success_url = reverse_lazy('economico:dato-umedida')

class UmedidaEdit(UpdateView):
    model = Umedida
    form_class = UmedidaForm
    success_url = reverse_lazy('economico:dato-umedida')

class UmedidaDelete(DeleteView):
    model = Umedida
    form_class = UmedidaForm
    success_url = reverse_lazy('economico:dato-umedida')