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


class Like(models.Model):
    likes = models.PositiveBigIntegerField()


class CreationDate(models.Model):
    # La diferencia entre [ auto_now_add ] y [ auto_now ] es que el atributo con add al final, no cambia la fecha desde que se añade, en cambio sin el ad al final, la fecha cambia despues de cada modificacion
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
        # Esto hace que el modelo hijo herede directamente la instancia

    def __str__(self):
        return str(self.creation_date)


class Description(CreationDate):
    title = models.CharField(max_length=50)
    genero = models.ManyToManyField(Genero)
    text_description = models.TextField(max_length=600)
    prologo = models.TextField(max_length=100)
    author = models.ManyToManyField(Author)
    imagen_portada = models.ImageField(
        blank=True, upload_to="portadas/", null=True)
    like = models.OneToOneField(
        Like, on_delete=models.CASCADE, blank=True, null=True)

    objects = CustomManager()

    def __str__(self):
        return str(self.title)


# Pendiente : 1/ hacer el modelo de la novela en si

# Modelo de Novela
