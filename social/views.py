from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from usuarios.models import PerfilUsuario
from social.models import Post, Like


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


@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        post.contenido = request.POST['contenido']
        
        if 'imagen' in request.FILES:
            post.imagen = request.FILES['imagen']
        
        try:
            post.save()
                    
        except Exception as e:
            print(e)
        
        return redirect('feed')

    return redirect('feed')


@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('feed')
    return HttpResponse(status=405)


@login_required
def perfil_usuario(request, perfil_id):
    perfil_usuario = get_object_or_404(PerfilUsuario, id=perfil_id)
    posts = Post.objects.filter(autor=perfil_usuario).order_by('-creado')
    
    usuarios = PerfilUsuario.objects.all()
    # Del array de usuarios quitar el usuario actual y los superusuarios
    usuarios = [usuario for usuario in usuarios if not usuario.user.is_superuser and usuario.user != request.user]
    

    return render(request, 'perfil.html', {
        'perfil_usuario': perfil_usuario,
        'posts': posts,
        'usuarios': usuarios,
    })


@login_required
def editar_perfil(request, perfil_id):
    perfil_usuario = get_object_or_404(PerfilUsuario, id=perfil_id)
    
    if request.method == "POST":
        perfil_usuario.bio = request.POST['bio']
        
        if 'imagen' in request.FILES:
            perfil_usuario.imagen = request.FILES['imagen']
        
        try:
            perfil_usuario.save()
                    
        except Exception as e:
            print(e)
        
    return redirect('perfil', perfil_id=perfil_id)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if request.method == 'POST':
        if Like.objects.filter(usuario=user, post=post).exists():
            # Si ya le gustó, eliminar el like
            Like.objects.filter(usuario=user, post=post).delete()
            liked = False
        else:
            # Si no le gustó, crear el like
            Like.objects.create(usuario=user, post=post)
            liked = True
        
        return JsonResponse({'liked': liked, 'likes_count': post.like_set.count()})

    return JsonResponse({'error': 'Invalid request'}, status=400)
