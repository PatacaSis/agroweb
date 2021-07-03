from django import forms
from .models import RubroGasto,RubroVenta,Subrubro,Umedida,Empleado,Cliente,Proveedor

class RubroGastoForm(forms.ModelForm):
    class Meta:
        model = RubroGasto
        fields = '__all__'

class RubroVentaForm(forms.ModelForm):
    class Meta:
        model = RubroVenta
        fields = '__all__'

class SubRubroGastoForm(forms.ModelForm):
    class Meta:
        model = Subrubro
        fields = '__all__'

class UmedidaForm(forms.ModelForm):
    class Meta:
        model = Umedida
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
