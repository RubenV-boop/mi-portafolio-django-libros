from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Libro")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    fecha_publicacion = models.DateField(verbose_name="Fecha de Publicación")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")

    class Meta:
        # Ordenar por fecha de publicación (los más nuevos primero)
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo

