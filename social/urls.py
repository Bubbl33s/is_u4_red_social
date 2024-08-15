from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('crear_post/', views.crear_post, name='crear_post'),
        path('editar_post/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
]
