from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name="predios"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:tipo_listado>", views.lista, name="listado"),
    path("detallado/<int:predio_id>", views.detallado, name="detallado")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)