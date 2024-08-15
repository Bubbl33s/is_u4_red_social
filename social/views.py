from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import PerfilUsuario
from social.models import Post


@login_required
def feed(request):
    usuarios = PerfilUsuario.objects.all()
    # Del array de usuarios quitar el usuario actual y los superusuarios
    usuarios = [usuario for usuario in usuarios if not usuario.user.is_superuser and usuario.user != request.user]
    
    # Obtener los posts
    posts = Post.objects.all().order_by('-creado')
    
    return render(request, 'feed.html', {
        'usuarios': usuarios,
        'posts': posts,
    })


# Posts
@login_required
def crear_post(request):
    if request.method == 'POST':
        # Crear un nuevo post
        post = Post(
            autor=request.user.perfilusuario,
            contenido=request.POST['contenido'],
            imagen=request.FILES.get('imagen', None)
        )
        
        try:
            post.save()
                    
        except Exception as e:
            print(e)
        
        return redirect('feed')
    
    return None
