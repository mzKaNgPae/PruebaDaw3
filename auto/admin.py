from django.contrib import admin
from .models import Auto,Marca,Competencia,Imagenes_Marca

# Register your models here.


admin.site.register(Auto)
admin.site.register(Marca)
admin.site.register(Competencia)
admin.site.register(Imagenes_Marca)