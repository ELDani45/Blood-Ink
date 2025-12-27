from django.db import models

# Create your models here.
# Que es un modelo: es una clase de pytohn que representa una tabla de nuestra base de datos.

# Estructura modelos de Novels:


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Genero(models.Model):
    gener = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.gener)

    objects = CustomManager()


class Description(models.Model):
    title = models.CharField(max_length=50)
    genero = models.ManyToManyField(Genero)
    text_description = models.TextField(max_length=600)
    prologo = models.TextField(max_length=100)
    imagen_portada = models.ImageField(
        blank=True, upload_to="portadas/", null=True)
    date_of_post = models.DateField(auto_now=True)

    objects = CustomManager()
# Pendiente : 1/ hacer el modelo de la novela en si
# 2/ INvestigar como crear l instancia que retorne las imagenes
