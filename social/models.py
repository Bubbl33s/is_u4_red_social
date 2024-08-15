from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('usuarios.PerfilUsuario', on_delete=models.CASCADE, related_name='posts')
    contenido = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(
        upload_to='post_images',
        blank=True,
        )

    def __str__(self):
        return f"{self.user.user.username} - {self.creado} - {self.texto[:20]}"
