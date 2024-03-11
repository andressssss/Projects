from django.db import models

# Create your models here.
class CMDB(models.Model):
    codigo = models.CharField(max_length=20)
    aplicacion = models.CharField(max_length=100)
    nombreSV = models.CharField(max_length=20)
    estadoApp = models.CharField(max_length=20)
    ipV4 = models.CharField(max_length=50)
    estadoipV4 = models.CharField(max_length=50)
    ambienteSV = models.CharField(max_length=50)
    rol = models.CharField(max_length=100)
    so = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return self.aplicacion

class eventos(models.Model):
    aplicacion = models.CharField(max_length=100)
    nombreSV = models.CharField(max_length=20)
    IP = models.CharField(max_length=50)
    SO = models.CharField(max_length=100)

    def __str__(self):
        return self.aplicacion

class lineabase(models.Model):
    codigo = models.CharField(max_length=20)
    aplicacion = models.CharField(max_length=200)
    instancia = models.CharField(max_length=100)
    ambienteSV = models.CharField(max_length=50)
    nombreSVHost = models.CharField(max_length=50)
    nombreSVOVM = models.CharField(max_length=50)
    ipV4 = models.CharField(max_length=50)

    def __str__(self):
        return self.aplicacion

class llave(models.Model):
    nombreAppCMDB = models.CharField(max_length=100)
    nombreAppEventos = models.CharField(max_length=100)
    nombrAppLB = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreAppCMDB

class CMDBvsEventos(models.Model):
    aplicacion = models.CharField(primary_key = True , max_length=100)
    ambienteSV = models.CharField(max_length=100)
    estadoApp = models.CharField(max_length=100)
    nombreSVCMDB = models.CharField(max_length=100)
    nombreSVEventos = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cmdbvseventos'

class LineabasevsEventos(models.Model):
    aplicacion = models.CharField(primary_key = True, max_length=100)
    ambienteSV = models.CharField(max_length=100)
    nombreSVLB = models.CharField(max_length=100)
    nombreSVEventos = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'lineabasevseventos'