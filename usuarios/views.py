from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages


# Inicio de sesión
def signin(request):
    if request.method == 'POST':
        usuario = authenticate(
            request,
            username=request.POST['usuario'],
            password=request.POST['contra'],
        )
        
        if usuario is None:
            messages.error(request, 'Credenciales incorrectas')
            
            return render(request, 'signin.html')
        
        else:
            login(request, usuario)
            messages.success(request, f'Sesión iniciada')
        
        return redirect('feed')
    
    logout(request)
    
    return render(request, 'signin.html')


# Registro
def signup(request):
    # Verificar el método
    if request.method == 'POST':
        # Verificar que ambos input del password sean iguales
        if request.POST['contra1'] == request.POST['contra2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['usuario'],
                    password=request.POST['contra1'],
                    first_name=request.POST['nombres'],
                    last_name=request.POST['apellidos']
                )

                user.save()
                login(request, user)

                return redirect('feed')

            # Manejar el error de usuario ya existente
            except IntegrityError:
                return render(request, 'signup.html')

        # Si las contraseñas no coinciden
        return render(request, 'signup.html')

    logout(request)
    
    return render(request, 'signup.html')


def temp(request):
    return render(request, 'temp.html')
