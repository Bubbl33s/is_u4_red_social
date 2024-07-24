from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Inicio de sesión
def signin(request):
    if request.method == 'GET':
        pass
    return render(request, 'signin.html')


# Registro
def signup(request):
    # Verificar el método
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
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

                return redirect('temp')

            # Manejar el error de usuario ya existente
            except IntegrityError:
                return render(request, 'signup.html', {
                    'error': 'El usuario ya existe'
                })

        # Si las contraseñas no coinciden
        return render(request, 'signup.html', {
            'error': 'Las contraseñas no coinciden'
        })


def temp(request):
    return render(request, 'temp.html')
