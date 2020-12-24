from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


class CategoryChoices(models.TextChoices):
    """ Listado de Categorias """
    URBANO = "URB", _("Urbano")
    RURAL = "RUR", _("Rural")


class ActiveChoices(models.TextChoices):
    """ Listado de Categorias """
    ACTIVO = "ACTI", _("Activo")
    INACTIVO = "INAC", _("Inactivo")


class Departamento(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre


class Barrio_vereda(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre


class Notaria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    circuito = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


class FormaAdquisicion(models.Model):
    nombre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre


class Condicion(models.Model):
    notaria = models.ForeignKey(
        Notaria, on_delete=models.CASCADE, blank=True, null=True)
    fecha_escritura = models.DateField(null=True, blank=True)
    escritura = models.CharField(max_length=50, null=False)
    modo_adquisicion = models.ForeignKey(
        FormaAdquisicion, on_delete=models.CASCADE, blank=True, related_name="modoAdquisicion")
    area_m2 = models.DecimalField(
        max_digits=7, decimal_places=0, null=False, default=0)
    area_hectareas = models.DecimalField(
        max_digits=7, decimal_places=0, null=False, default=0)
    propietario = models.CharField(max_length=50, null=True, blank=True)
    documento_identidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"escritura: {self.escritura} Area: {self.area_hectareas} hm2 + {self.area_m2} m2"


class Predio(models.Model):
    """ Listado de predios"""
    matricula_inmoviliaria_1 = models.IntegerField(null=False,
                                                   help_text="primer grupo de dígitos de izquierda a derecha",
                                                   validators=[MinValueValidator(0),
                                                               MaxValueValidator(9999)])
    matricula_inmoviliaria_2 = models.IntegerField(null=False,
                                                   help_text="segundo grupo de dígitos de izquierda a derecha",
                                                   validators=[MinValueValidator(0),
                                                               MaxValueValidator(9999)])
    category = models.CharField(max_length=3,
                                choices=CategoryChoices.choices, default=CategoryChoices.URBANO, blank=False)
    dataFile = models.FileField(upload_to='data/')
    nombre = models.CharField(max_length=50, default='Sin Identificar')
    cedula_catastral_1 = models.IntegerField(default=0, null=False,
                                             help_text="primer grupo de dígitos de izquierda a derecha",
                                             validators=[MinValueValidator(0),
                                                         MaxValueValidator(99)])
    cedula_catastral_2 = models.IntegerField(default=1, null=False,
                                             help_text="segundo grupo de dígitos de izquierda a derecha",
                                             validators=[MinValueValidator(0),
                                                         MaxValueValidator(99)])
    cedula_catastral_3 = models.IntegerField(default=1, null=False,
                                             help_text="tercer grupo de dígitos de izquierda a derecha",
                                             validators=[MinValueValidator(0),
                                                         MaxValueValidator(9999)])
    cedula_catastral_4 = models.IntegerField(null=False,
                                             help_text="cuarto grupo de dígitos de izquierda a derecha",
                                             validators=[MinValueValidator(0),
                                                         MaxValueValidator(9999)])
    cedula_catastral_5 = models.IntegerField(default=0, null=False,
                                             help_text="quinto grupo de dígitos de izquierda a derecha",
                                             validators=[MinValueValidator(0),
                                                         MaxValueValidator(999)])
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, blank=False)
    municipio = models.ForeignKey(
        Municipio, on_delete=models.CASCADE, blank=False)
    barrio_vereda = models.ForeignKey(
        Barrio_vereda, on_delete=models.CASCADE, blank=False, related_name="barrio")
    direccion = models.CharField(max_length=50, blank=False)
    estado_folio = models.CharField(max_length=4,
                                    choices=ActiveChoices.choices, default=ActiveChoices.INACTIVO, blank=False)
    fecha_apertura = models.DateField(null=True)
    documento_radicacion_1 = models.IntegerField(default=0, null=False,
                                                 help_text="primer grupo de dígitos de izquierda a derecha",
                                                 validators=[MinValueValidator(0),
                                                             MaxValueValidator(99)])
    documento_radicacion_2 = models.IntegerField(default=0, null=False,
                                                 help_text="segundo grupo de dígitos de izquierda a derecha",
                                                 validators=[MinValueValidator(0),
                                                             MaxValueValidator(99999)])
    condicion_inicial = models.OneToOneField(
        Condicion, on_delete=models.CASCADE, null=True, related_name="estadoInicial")
    predio_matriz = models.CharField(max_length=50, null=True)
    procede_del_predio = models.CharField(max_length=50, null=True, blank=True)
    condicion_actual = models.OneToOneField(
        Condicion, on_delete=models.CASCADE, null=True, related_name="estadoActual")
    total_anotaciones = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.nombre

    def num_cedula_catastral(self):
        return f"{self.cedula_catastral_1:02}-{self.cedula_catastral_2:02}-{self.cedula_catastral_3:04}-{self.cedula_catastral_4:04}-{self.cedula_catastral_5:03}"

    def num_matricula_inmoviliaria(self):
        return f"{self.matricula_inmoviliaria_1:04}-{self.matricula_inmoviliaria_2:04}"

    def num_documento_radicacion(self):
        return f"{self.documento_radicacion_1:02}-{self.documento_radicacion_2:05}"


@receiver(post_delete, sender=Predio)
def predio_delete(sender, instance, **kwargs):
    """ Borra los ficheros de los archivos que se eliminan. """
    instance.dataFile.delete(False)
