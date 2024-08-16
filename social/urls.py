from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('editar_post/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
    path('perfil/<int:perfil_id>/', views.perfil_usuario, name='perfil'),
    path('perfil/editar/<int:perfil_id>/', views.editar_perfil, name='editar_perfil'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
