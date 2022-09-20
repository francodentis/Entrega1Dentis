from django.db import models

# Create your models here.

class Salones(models.Model):
    salon=models.CharField(max_length=40)
    ciudad=models.CharField(max_length=40)
    capacidad=models.IntegerField()

class Vestidos(models.Model):
    modelo=models.CharField(max_length=40)
    color=models.CharField(max_length=40)
    modista=models.CharField(max_length=40)
    precio=models.IntegerField()

class LunaDeMiel(models.Model):
    destino=models.CharField(max_length=40)
    