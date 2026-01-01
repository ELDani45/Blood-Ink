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


class Author(models.Model):
    firts_names = models.CharField('Nombres del Autor', max_length=100)
    lasts_names = models.CharField('Apellidos del Autor', max_length=100)
    age = models.PositiveBigIntegerField(verbose_name='Edad')

    def __str__(self):
        return str(self.firts_names)
# Modelo de descripcion de las novelas
# - Pendienrte:
# * Realcionar este modelo con el modelo de la novela
# * Hacer representascion visual en excalidraw


class Description(models.Model):
    title = models.CharField(max_length=50)
    genero = models.ManyToManyField(Genero)
    text_description = models.TextField(max_length=600)
    prologo = models.TextField(max_length=100)
    author = models.ManyToManyField(Author)
    imagen_portada = models.ImageField(
        blank=True, upload_to="portadas/", null=True)
    date_of_post = models.DateField(auto_now=True)

    objects = CustomManager()

    def __str__(self):
        return str(self.title)
# Pendiente : 1/ hacer el modelo de la novela en si

# Modelo de Novela


class Novela(models.Model):
    personajes = models.ImageField(blank=True)
