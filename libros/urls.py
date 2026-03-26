from django.urls import path
from . import views

urlpatterns = [
    # Ruta: /libros/
    path('', views.listar_libros, name='listar_libros'),
    
    # Ruta: /libros/crear/
    path('crear/', views.crear_libro, name='crear_libro'),
    
    # Ruta: /libros/editar/<id>/ (Parámetro dinámico)
    path('editar/<int:id>/', views.editar_libro, name='editar_libro'),
    
    # Ruta: /libros/eliminar/<id>/ (Parámetro dinámico)
    path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]
