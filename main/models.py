from django.db import models

# Create your models here.

class Casa(models.Model):
    baths = models.IntegerField(null=False,default=1)
    habitaciones = models.IntegerField(null=False,default=1)
    metros = models.IntegerField(null=False)
    foto = models.ImageField(upload_to='casas/')
    materiales = models.CharField(max_length=70)
    estilo = models.CharField(max_length=70)
    precio = models.DecimalField(null=False,decimal_places=2,max_digits=10)
    descripcion = models.CharField(max_length=250,null=True)

    def __str__(self):
        return f'Habitaciones: {self.habitaciones} - Baños: {self.baths}'

    # class Meta:
    #     verbose_name_plural = 'atenciones'


class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre+" "+self.apellido

