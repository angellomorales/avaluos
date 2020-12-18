from django.contrib import admin
from predios.models import Predio

class PredioAdmin(admin.ModelAdmin):
    list_display=("title","category")

admin.site.register(Predio,PredioAdmin)
