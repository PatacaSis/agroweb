from django.contrib import admin
from .models import ProdLeche,Alimento,ExistenciaTambo,ExistenciaRecria


class ProdLecheAdmin(admin.ModelAdmin):
    list_display = ['fecha','venta','consumo','lts_total','ltsxvo']

class ExistenciaTamboAdmin(admin.ModelAdmin):
    list_display = ['fecha','vo','vs','vtotal','vaqpp','to','tg']

class ExistenciaRecriaAdmin(admin.ModelAdmin):
    list_display = ['fecha','terneros','recria','vaq','vaqcserv','nov','rt']

class AlimentoAdmin(admin.ModelAdmin):
    list_display = ['alimento','ms','pt']

admin.site.register(ProdLeche,ProdLecheAdmin)
admin.site.register(Alimento,AlimentoAdmin)
admin.site.register(ExistenciaTambo,ExistenciaTamboAdmin)
admin.site.register(ExistenciaRecria,ExistenciaRecriaAdmin)