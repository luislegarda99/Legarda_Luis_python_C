from django.db import models
import datetime as dt

# Create your models here.

class Productos(models.Model):
    
    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"
        
    nombre = models.CharField("Nombre", max_length=300, blank=False)
    descripcion = models.CharField("Descripción", max_length=300, blank=False)
    precio = models.IntegerField("Precio", blank=False)
    fecha_registro = models.DateField("Fecha de registro",  default=dt.date.today())
    estatus = models.BooleanField("Estatus",  default=False, choices=[
        (True, "Disponible"), 
        (False, "No Disponible"),
    ])

def _str_(self):
    return self.nombre