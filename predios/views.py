from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Predio, CategoryChoices


def index(request):

    return render(request, "predios/index.html")


def lista(request, tipo_listado):
    if request.method == "GET":
        tipoLista = request.GET["tipo"]
        listado = Predio.objects.filter(category=tipo_listado)

    context = {
        "listado": listado
    }
    return render(request, "predios/listado.html", context)


def detallado(request, predio_id):
    try:
        predioActual=Predio.objects.get(pk=predio_id)
    except ObjectDoesNotExist:
        predioActual=None
    
    context = {
        "predio":predioActual
    }
    return render(request, "predios/detallado.html",context)
