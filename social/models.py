from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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


class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'post')  # Asegura que un usuario no pueda dar like más de una vez a un post

    def __str__(self):
        return f"{self.usuario.username} likes {self.post.id}"
    