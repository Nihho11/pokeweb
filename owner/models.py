from django.db import models


# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField
    pais = models.CharField(max_length=25, default='')
    descripcion = models.CharField(max_length=50, default='')
    dni = models.CharField(max_length=8, default='00000000')
    vigente = models.BooleanField(default=True)