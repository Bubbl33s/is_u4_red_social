from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('crear_post/', views.crear_post, name='crear_post'),
]
