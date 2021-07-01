from django import forms
from .models import RubroGasto,RubroVenta,Subrubro,Umedida

class RubroGastoForm(forms.ModelForm):
    class Meta:
        model = RubroGasto
        fields = '__all__'

class RubroVentaForm(forms.ModelForm):
    class Meta:
        model = RubroVenta
        fields = '__all__'
    