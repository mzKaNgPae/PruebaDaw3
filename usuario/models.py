from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from django.conf import settings

# Create your models here.

class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='bd/usuarios', default='bd/usuarios/no-img.jpg')
    imagen_auto = models.ImageField(upload_to='bd/usuarios', null=True)
    rut = models.CharField(
        max_length=10,
        primary_key=True,
        validators=[
            RegexValidator(r'^\d{7,8}$')
        ])
    dv = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9K]$')])
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, null=True)
    telefono = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^(\+56[1-9]{1,2}|)[1-9][0-9]{7}$')]
    )
    correo = models.EmailField()
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE,related_name='tipo')

    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno}'

    def get_rut(self):
        return f'{self.rut}-{self.dv}'
    
    def get_biografia(self):
        return Biografia.objects.filter(usuario=self.rut)

class Biografia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.usuario} - {self.id}'


