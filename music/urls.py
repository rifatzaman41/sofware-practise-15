from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.musician_list,name='musician_list'),
     path('add/',views.musician_detail,name='musician_detail'),
      path('add/',views.musician_create,name='musician_create'),
       path('add/',views.musician_delete,name='musician_delete'),
       
]
