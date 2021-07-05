from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import RubroGasto,RubroVenta,Subrubro,Umedida,Empleado,Cliente,Proveedor,Gasto
from .forms import RubroGastoForm,RubroVentaForm,SubRubroGastoForm,UmedidaForm,EmpleadoForm,ClienteForm,ProveedorForm,GastoForm
# Datos de configuración -----------------------------------------------------------
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

def EmpleadoList(request):
    empleados = Empleado.objects.filter(estado=True)
    return render(request, 'economico/empleado_list.html', {'empleados':empleados})

class EmpleadoCrear(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('economico:dato-empleado')

class EmpleadoEdit(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('economico:dato-empleado')

class EmpleadoDelete(DeleteView):
    model = Empleado

    def post(self,request, pk,*args,**kwargs):
        object = Empleado.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:dato-empleado')

def ProveedorList(request):
    proveedores = Proveedor.objects.filter(estado=True)
    return render(request, 'economico/proveedor_list.html', {'proveedores':proveedores})

class ProveedorCrear(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('economico:dato-proveedor')

class ProveedorEdit(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('economico:dato-proveedor')

class ProveedorDelete(DeleteView):
    model = Proveedor

    def post(self,request, pk,*args,**kwargs):
        object = Proveedor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:dato-proveedor')

def ClienteList(request):
    clientes = Cliente.objects.filter(estado=True)
    return render(request, 'economico/cliente_list.html', {'clientes':clientes})

class ClienteCrear(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('economico:dato-cliente')

class ClienteEdit(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('economico:dato-cliente')

class ClienteDelete(DeleteView):
    model = Cliente

    def post(self,request, pk,*args,**kwargs):
        object = Cliente.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:dato-cliente')

# Datos de carga de gastos e ingresos -------------------------------------------------

def GastosList(request):
    gastos = Gasto.objects.filter(estado=True)
    return render(request, 'economico/gasto_list.html', {'gastos':gastos})

class GastoCrear(CreateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy('economico:gasto')

class GastoEdit(UpdateView):
    model = Cliente
    form_class = GastoForm
    success_url = reverse_lazy('economico:gasto')

class GastoDelete(DeleteView):
    model = Gasto

    def post(self,request, pk,*args,**kwargs):
        object = Gasto.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:gasto')