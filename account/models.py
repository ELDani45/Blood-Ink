from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image_profile = models.ImageField(
        upload_to='profiles_images',
        default='profiles_images/icono-de-foto-perfil-predeterminada-en-alta-resolución-360167031.webp',
        blank=True
    )
    social_network = models.TextField(max_length=20, blank=True)
    about_me = models.CharField(max_length=200, blank=True)
    favorite_genes = models.ManyToManyField(
        'novels.Genero', related_name='generos', blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
