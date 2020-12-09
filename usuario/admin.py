from django.contrib import admin
from .models import Usuario,TipoUsuario,Biografia

# Register your models here.


admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Biografia)