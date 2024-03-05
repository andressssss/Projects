from django.db import models

# Create your models here.

class Aplicaciones(models.Model):
    identificacion = models.IntegerField()
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    nombreSV = models.CharField(max_length=100)

class lineabase(models.Model):
    text = models.TextField()

from django.db import models

class Tcmdbapp(models.Model):
    codApp = models.CharField(max_length=20)
    nomAppCmdb = models.CharField(max_length=100)
    nomServCmdb = models.CharField(max_length=20)
    Estado = models.CharField(max_length=20)
    ambi = models.CharField(max_length=50)
    ubica = models.CharField(max_length=50)

    def __str__(self):
        return self.nomAppCmdb

class Tevento(models.Model):
    nomAppEven = models.CharField(max_length=100)
    nomServEven = models.CharField(max_length=20)
    IpServEven = models.CharField(max_length=50)
    SO = models.CharField(max_length=100)

    def __str__(self):
        return self.nomAppEven

class Tlb(models.Model):
    codApp = models.CharField(max_length=20)
    app = models.CharField(max_length=200)
    insta = models.CharField(max_length=100)
    ambi = models.CharField(max_length=50)
    nomovm = models.CharField(max_length=50)
    nomhost = models.CharField(max_length=50)
    IP = models.CharField(max_length=50)

    def __str__(self):
        return self.app

class Tllavep(models.Model):
    nomAppEven = models.CharField(max_length=100)
    nomAppCmdb = models.CharField(max_length=100)
    xx = models.CharField(max_length=10)

    def __str__(self):
        return self.nomAppEven

class Tsolici1(models.Model):
    orden = models.CharField(max_length=20)
    idReq = models.CharField(max_length=20)
    Fcrea = models.DateTimeField()
    Fcom = models.DateTimeField()
    FCierre = models.DateTimeField()
    FUmod = models.DateTimeField()
    FReaper = models.DateTimeField()
    IdSede = models.CharField(max_length=10)
    TSede = models.CharField(max_length=20)
    NSede = models.CharField(max_length=100)
    Depto = models.CharField(max_length=50)
    Priori = models.CharField(max_length=15)
    HSede = models.CharField(max_length=150)
    NClien = models.CharField(max_length=100)
    Email = models.EmailField(max_length=60)
    Email1 = models.EmailField(max_length=60)
    ServAfec = models.CharField(max_length=60)
    Resu = models.CharField(max_length=500)
    Notas = models.TextField()
    Solu = models.TextField()
    Esta = models.CharField(max_length=30)
    MotiE = models.CharField(max_length=40)
    GrupoA = models.CharField(max_length=60)
    AsigA = models.CharField(max_length=50)
    FuenR = models.CharField(max_length=30)
    CateO1 = models.CharField(max_length=40)
    CateO2 = models.CharField(max_length=90)
    CateO3 = models.CharField(max_length=90)
    CateP1 = models.CharField(max_length=40)
    CateP2 = models.CharField(max_length=100)
    CateP3 = models.CharField(max_length=100)
    Nans = models.CharField(max_length=80)
    MSLAmin = models.FloatField()
    Tansmin = models.FloatField()
    Tansdias = models.FloatField()
    FestaPen = models.DateTimeField()
    Tpenmin = models.FloatField()
    TTAnsmin = models.FloatField()
    EstaAns = models.CharField(max_length=20)
    PorcCumAns = models.FloatField()

    def __str__(self):
        return self.orden
