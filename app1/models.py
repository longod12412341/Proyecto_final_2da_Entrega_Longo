from django.db import models

# Create your models here.
class celularnuevo(models.Model):
    email = models.EmailField()
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    imagen = models.ImageField(upload_to='celulares/', null=True)
    estado = models.CharField(max_length=100, null=True)
    def __str__(self):
                return f" Modelo: {self.modelo}| email: {self.email} | telefono: {self.telefono}"