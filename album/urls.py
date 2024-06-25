from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.album_detail,name='album_detail'),
    path('add/',views.album_create,name='album_create'),
    path('add/',views.album_delete,name='album_delete'),
    
]