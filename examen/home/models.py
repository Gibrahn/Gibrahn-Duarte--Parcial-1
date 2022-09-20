from django.db import models

# Create your models here.
class Equipos(models.Model):
  nombre = models.CharField(max_length=200)
  categoria = models.CharField(max_length=200)
  capitan = models.CharField(max_length=200)


  def __str__(self):
    return self.nombre

class Estadios(models.Model):
  nombre = models.CharField(max_length=200)
  ubicacion = models.CharField(max_length=200)
  owner = models.CharField(max_length=200)

  def __str__(self):
    return self.nombre    

class Jugadores(models.Model):
  nombre = models.CharField(max_length=200)
  edad = models.CharField(max_length=200)
  equipo = models.CharField(max_length=200)

  def __str__(self):
    return self.nombre    