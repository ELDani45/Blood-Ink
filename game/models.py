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

    def __str__(self):
        return str(self.title)


def page_upload_path(instance, filename):
    return f"novelas/{instance.novela.id}/{filename}"


class Scenes(models.Model):
    novel = models.ForeignKey(
        Novel_game, on_delete=models.CASCADE, related_name='pages')

    scene_number = models.PositiveIntegerField(default=0)
    background_scene = models.ImageField(upload_to='page_upload_path/')

    class Meta:  # METADATOS = Aqui se define todo lo que no es un campo
        ordering = ['scene_number']

    def __str__(self):
        return str(self.novel)


class Choice(models.Model):
    """Decisiones al final de una escena que llevan a otra."""
    source_scene = models.ForeignKey(
        Scenes, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(
        max_length=255, help_text="Lo que el jugador lee en el botón")
    destination_scene = models.ForeignKey(
        Scenes, related_name='incoming_choices', on_delete=models.CASCADE)

    def __str__(self):
        return f"De {self.source_scene} a {self.destination_scene}"


class Dialogue(models.Model):
    scene = models.ForeignKey(
        Scenes, related_name='dialogues', on_delete=models.CASCADE)
    character = models.ForeignKey(
        Characters, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    order = models.PositiveIntegerField(
        default=0, help_text="Orden en que aparece el diálogo")

    class Meta:
        ordering = ['order']
