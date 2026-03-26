from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # Para enviar notificaciones al usuario
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required 


def listar_libros(request):
    # Capturamos lo que el usuario escribe en el buscador
    query = request.GET.get('q')
    if query:
        # Filtramos por título que contenga el texto (ignore case)
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()
    
    return render(request, 'libros/listar_libros.html', {'libros': libros, 'query': query})

@login_required # Solo usuarios logueados pueden ver el formulario
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Libro añadido exitosamente!')
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario_libro.html', {'form': form, 'accion': 'Añadir Nuevo'})

@login_required
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.info(request, 'El libro ha sido actualizado.')
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario_libro.html', {'form': form, 'accion': 'Editar'})

@login_required
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        messages.warning(request, 'El libro ha sido eliminado del sistema.')
        return redirect('listar_libros')
    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro})
