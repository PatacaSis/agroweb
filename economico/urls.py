from django.urls import path
from .views import RubroGastoList,RubroGastoEdit,RubroGastoCrear,RubroGastoDelete, RubroVentaEdit,RubroVentaList,RubroVentaCrear,RubroVentaDelete



app_name = 'economico'

urlpatterns = [
    path('rubro/gastos/', RubroGastoList.as_view(), name='rubro-gasto'),
    path('rubro/gastos/crear/', RubroGastoCrear.as_view(), name='rubro-gasto-crear'),
    path('rubro/gastos/editar/<int:pk>/', RubroGastoEdit.as_view(), name='rubro-gasto-edit'),
    path('rubro/gastos/borrar/<int:pk>/', RubroGastoDelete.as_view(), name='rubro-gasto-delete'),

    path('rubro/ventas/', RubroVentaList.as_view(), name='rubro-venta'),
    path('rubro/ventas/crear/', RubroVentaCrear.as_view(), name='rubro-venta-crear'),
    path('rubro/ventas/editar/<int:pk>/', RubroVentaEdit.as_view(), name='rubro-venta-edit'),
    path('rubro/ventas/borrar/<int:pk>/', RubroVentaDelete.as_view(), name='rubro-venta-delete'),
]
