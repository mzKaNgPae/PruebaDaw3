from django.db import models

# Create your models here.


class Auto(models.Model):
    imagen = models.ImageField(upload_to='bd/autos')
    marca = models.CharField(max_length=70)
    modelo = models.CharField(max_length=70)
    anno = models.CharField(max_length=4,null=True)
    velocidad_partida = models.CharField(max_length=50,null=True)
    velocidad_maxima = models.DecimalField(decimal_places=2,max_digits=6,null=True)
    precio = models.DecimalField(decimal_places=2,max_digits=10,null=True)
    descripcion = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.marca + ' ' + self.modelo