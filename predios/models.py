from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_delete
from django.dispatch import receiver

class CategoryChoices(models.TextChoices):
    """ Listado de Categorias """
    URBANO = "URB", _("Urbano")
    RURAL = "RUR", _("Rural")

class Predio(models.Model):
    """ Listado de predios"""
    category = models.CharField(
        max_length=3, choices=CategoryChoices.choices, default=CategoryChoices.URBANO, blank=False)
    title = models.CharField(max_length=50, default='Sin Identificar')
    dataFile = models.FileField(upload_to='data/')

    def __unicode__(self):
        return self.title
    
@receiver(post_delete,sender=Predio)
def predio_delete(sender, instance, **kwargs):
    """ Borra los ficheros de los archivos que se eliminan. """
    instance.dataFile.delete(False)