from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario


# Create your views here.
@login_required
def home(request):
    return render(request, "core/home.html")

@login_required
def about(request):
    ctx = {}
    admins = Usuario.objects.all().filter(tipo_usuario=1)
    ctx['admins'] = admins
    return render(request, "core/about.html", ctx)
    
@login_required
def contact(request):
    return render(request, "core/contacto.html")
    