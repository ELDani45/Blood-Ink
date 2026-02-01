from django.db import models


# Create your models here.


class Characters(models.Model):
    name = models.CharField(max_length=50)
    characters_body = models.ImageField(upload_to='characters/')

    def __str__(self):
        return str(self.name)


class Novel_game(models.Model):
    title = models.CharField(max_length=50)
    character = models.ManyToManyField(Characters)


class Scenes(models.Model):
    novel = models.ForeignKey(
        Novel_game, on_delete=models.CASCADE, related_name='scenes')

    scene_number = models.PositiveIntegerField(default=0)
    background_scene = models.ImageField(upload_to='backgrounds/')

    class Meta:  # METADATOS = Aqui se define todo lo que no es un campo
        ordering = ['scene_number']
