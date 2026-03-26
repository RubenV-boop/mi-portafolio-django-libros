from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # Columnas que se verán en el listado del admin
    list_display = ('titulo', 'autor', 'isbn', 'fecha_publicacion')
    # Filtros laterales
    list_filter = ('autor', 'fecha_publicacion')
    # Buscador en el admin
    search_fields = ('titulo', 'isbn')
