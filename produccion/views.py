from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import ProdLeche,Alimento,ExistenciaTambo,ExistenciaRecria
from .forms import ProdLecheForm,AlimentoForm,ExistenciaTamboForm,ExistenciaRecriaForm,FechasForm

#====== Vistas de la aplicacion produccion =============
#====== Vistas para Produccion de Leche ================

class ProdLecheList(ListView):
    model = ProdLeche

def Pl_fechas(request,inicio,fin):
    form = FechasForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            inicio = form.cleaned_data['inicio']
            fin = form.cleaned_data['final']
    
    qs = ProdLeche.objects.filter(fecha__range=[inicio, fin])
    
    suma = 0
    for dato in qs:
        d = dato.lts_total
        suma = suma + d
    ctx = {'qs': qs, 'suma': suma, 'form':form}
    return render(request, 'produccion/prueba.html', ctx)  
         
class ProdLecheCreate(CreateView):
    model = ProdLeche
    form_class = ProdLecheForm
    success_url = reverse_lazy('produccion:leche_list')

class ProdLecheUpdate(UpdateView):
    model = ProdLeche
    form_class = ProdLecheForm
    success_url = reverse_lazy('produccion:leche_list')

class ProdLecheDelete(DeleteView):
    model = ProdLeche
    success_url = reverse_lazy('produccion:leche_list')


#====== Vistas para Existencias ================

class Existencia(ListView):
    model = ExistenciaTambo
    template_name = 'produccion/existenciatambo_list.html'

class ExistenciaCreate(CreateView):
    model = ExistenciaTambo
    form_class = ExistenciaTamboForm
    success_url = reverse_lazy('produccion:existenciatambo-list')

class ExistenciaUpdate(UpdateView):
    model = ExistenciaTambo
    form_class = ExistenciaTamboForm
    success_url = reverse_lazy('produccion:existenciatambo-list')

class ExistenciaDelete(DeleteView):
    model = ExistenciaTambo
    success_url =  reverse_lazy('produccion:existenciatambo-list')
#--------------------------------------------------------------------
class Recria(ListView):
    model = ExistenciaRecria
    template_name = 'produccion/existenciarecria_list.html'

class RecriaCreate(CreateView):
    model = ExistenciaRecria
    form_class = ExistenciaRecriaForm
    success_url = reverse_lazy('produccion:recria-list')

class RecriaUpdate(UpdateView):
    model = ExistenciaRecria
    form_class = ExistenciaRecriaForm
    success_url = reverse_lazy('produccion:recria-list')

class RecriaDelete(DeleteView):
    model = ExistenciaRecria
    success_url =  reverse_lazy('produccion:recria-list')  

#====== Vistas para Tipos de Alimentos ================

class AlimentoList(ListView):
    model = Alimento

class AlimentoCreate(CreateView):
    model = Alimento
    form_class = AlimentoForm
    success_url = reverse_lazy('produccion:alimento')

class AlimentoUpdate(UpdateView):
    model = Alimento
    form_class = AlimentoForm
    success_url = reverse_lazy('produccion:alimento')

class AlimentoDelete(DeleteView):
    model = Alimento
    success_url = reverse_lazy('produccion:alimento')

   