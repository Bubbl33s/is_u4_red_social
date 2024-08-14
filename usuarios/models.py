from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    imagen = models.ImageField(
        upload_to='profile_images',
        blank=True,
        default='../static/img/default_pfp.png'
        )

    def __str__(self):
        return self.user.username
