from django.db import models

# Create your models here.

class Aplicaciones(models.Model):
    identificacion = models.IntegerField()
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    nombreSV = models.CharField(max_length=100)