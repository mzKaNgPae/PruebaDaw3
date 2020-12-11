from django.db import models
from django.urls import reverse
# Create your models here.


class Marca(models.Model):
    PAISES_CHOICES = ((0,'No definido'),(1,'Alemania'),(2,'Italia'),(3,'Reino Unido'),(4,'Estados Unidos'),(5,'Japon'),(6,'Francia'))
    marca = models.CharField(max_length=70)
    pais = models.PositiveSmallIntegerField(choices=PAISES_CHOICES, default=0)
    historia = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.marca

class Imagenes_Marca(models.Model):
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='bd/marcas')

    def __str__(self):
        return f'{self.marca} - {self.id}'

class Auto(models.Model):
    imagen = models.ImageField(upload_to='bd/autos',null=True,blank=True)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    modelo = models.CharField(max_length=70)
    anno = models.CharField(max_length=4)
    velocidad_partida = models.CharField(max_length=50)
    velocidad_maxima = models.CharField(max_length=6)
    precio = models.DecimalField(decimal_places=2,max_digits=10)
    descripcion = models.CharField(max_length=500, null=True,blank=True)
    
    def __str__(self):
        return self.marca.marca + ' ' + self.modelo

    def get_absolute_url(self):
        return reverse('modificar-auto', kwargs={'pk': self.pk})
        
class Competencia(models.Model):
    nombre = models.CharField(max_length=70)
    victorias = models.IntegerField(default=0)
    marca_campion = models.ForeignKey(Marca,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.marca_campion.marca