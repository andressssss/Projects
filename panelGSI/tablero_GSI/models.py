from django.db import models

# Create your models here.

class Aplicaciones(models.Model):
    identificacion = models.IntegerField()
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    nombreSV = models.CharField(max_length=100)
class CMDB(models.Model):
    codApp = models.CharField(max_length=20)
    nomAppCmdb = models.CharField(max_length=100)
    nomServCmdb = models.CharField(max_length=20)
    Estado = models.CharField(max_length=20)
    ambi = models.CharField(max_length=50)
    ubica = models.CharField(max_length=50)

    def __str__(self):
        return self.nomAppCmdb

class eventos(models.Model):
    nomAppEven = models.CharField(max_length=100)
    nomServEven = models.CharField(max_length=20)
    IpServEven = models.CharField(max_length=50)
    SO = models.CharField(max_length=100)

    def __str__(self):
        return self.nomAppEven

class lineabase(models.Model):
    codApp = models.CharField(max_length=20)
    app = models.CharField(max_length=200)
    insta = models.CharField(max_length=100)
    ambi = models.CharField(max_length=50)
    nomovm = models.CharField(max_length=50)
    nomhost = models.CharField(max_length=50)
    IP = models.CharField(max_length=50)

    def __str__(self):
        return self.app

class llave(models.Model):
    nomAppEven = models.CharField(max_length=100)
    nomAppCmdb = models.CharField(max_length=100)
    xx = models.CharField(max_length=10)

    def __str__(self):
        return self.nomAppEven