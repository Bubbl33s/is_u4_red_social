from django.shortcuts import render, redirect
from usuarios.models import PerfilUsuario

# Create your views here.
def feed(request):
    usuarios = PerfilUsuario.objects.all()
    # Del array de usuarios quitar el usuario actual y los superusuarios
    usuarios = [usuario for usuario in usuarios if not usuario.user.is_superuser and usuario.user != request]
    
    return render(request, 'feed.html', {
        'usuarios': usuarios
    })
