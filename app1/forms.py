from django import forms
from .models import *

class celularNuevoform(forms.Form):
    email = forms.EmailField()
    modelo = forms.CharField(max_length=100)
    descripcion = forms.TextField()
    telefono = forms.CharField(max_length=20)
    precio = forms.DecimalField(max_digits=20, decimal_places=2,null=True)
    imagen =forms.ImageField(upload_to='celulares/', null=True)
    estado = models.CharField(max_length=100, null=True)