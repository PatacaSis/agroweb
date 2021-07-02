from django.urls import path
from .views import RubroGastoList,RubroGastoEdit,RubroGastoCrear,RubroGastoDelete, RubroVentaEdit,RubroVentaList,RubroVentaCrear,RubroVentaDelete,SubrubroGastoList,SubrubroGastoCrear,SubrubroGastoEdit,SubrubroGastoDelete, UmedidaList,UmedidaCrear,UmedidaEdit,UmedidaDelete



app_name = 'economico'

urlpatterns = [
    path('rubro/gastos/', RubroGastoList.as_view(), name='rubro-gasto'),
    path('rubro/gastos/crear/', RubroGastoCrear.as_view(), name='rubro-gasto-crear'),
    path('rubro/gastos/editar/<int:pk>/', RubroGastoEdit.as_view(), name='rubro-gasto-edit'),
    path('rubro/gastos/borrar/<int:pk>/', RubroGastoDelete.as_view(), name='rubro-gasto-delete'),

    path('subrubro/gastos/', SubrubroGastoList.as_view(), name='subrubro-gasto'),
    path('subrubro/gastos/crear/', SubrubroGastoCrear.as_view(), name='subrubro-gasto-crear'),
    path('subrubro/gastos/editar/<int:pk>/', SubrubroGastoEdit.as_view(), name='subrubro-gasto-edit'),
    path('subrubro/gastos/borrar/<int:pk>/', SubrubroGastoDelete.as_view(), name='subrubro-gasto-delete'),

    path('rubro/ventas/', RubroVentaList.as_view(), name='rubro-venta'),
    path('rubro/ventas/crear/', RubroVentaCrear.as_view(), name='rubro-venta-crear'),
    path('rubro/ventas/editar/<int:pk>/', RubroVentaEdit.as_view(), name='rubro-venta-edit'),
    path('rubro/ventas/borrar/<int:pk>/', RubroVentaDelete.as_view(), name='rubro-venta-delete'),

    path('datos/u_medida/', UmedidaList.as_view(), name='dato-umedida'),
    path('datos/u_medida/crear/', UmedidaCrear.as_view(), name='dato-umedida-crear'),
    path('datos/u_medida/editar/<int:pk>/', UmedidaEdit.as_view(), name='dato-umedida-edit'),
    path('datos/u_medida/borrar/<int:pk>/', UmedidaDelete.as_view(), name='dato-umedida-delete'),
]
