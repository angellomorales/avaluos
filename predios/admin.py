from django.contrib import admin
from predios.models import Predio,Municipio,Barrio_vereda,Departamento,Condicion,FormaAdquisicion,Notaria

class PredioAdmin(admin.ModelAdmin):
    list_display=("nombre","category","barrio_vereda", "direccion","estado_folio","condicion_actual")


class CondicionAdmin(admin.ModelAdmin):
    list_display=("notaria","fecha_escritura","escritura","modo_adquisicion","area_hectareas","area_m2","propietario","documento_identidad")

class NotariaAdmin(admin.ModelAdmin):
    list_display=("nombre","circuito")

admin.site.register(Predio,PredioAdmin)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Barrio_vereda)
admin.site.register(Condicion,CondicionAdmin)
admin.site.register(Notaria,NotariaAdmin)
admin.site.register(FormaAdquisicion)

