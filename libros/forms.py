from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        # Definimos qué campos del modelo aparecerán en el formulario
        fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
        
        # Agregamos un widget para que el campo de fecha sea un calendario en el navegador
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }
