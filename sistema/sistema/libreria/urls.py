from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
]