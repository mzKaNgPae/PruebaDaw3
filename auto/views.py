from django.shortcuts import render
from .models import Auto,Competencia
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def tablas(request):
    ctx = {}
    top10 = Auto.objects.all().order_by('-velocidad_maxima')[0:10]
    ctx['top10'] = top10
    competencias = Competencia.objects.all().order_by('nombre','-victorias')
    ctx['competencias'] = competencias

    return render(request, 'tablas.html', ctx)

@login_required
def historia(request):
    ctx = {}
    return render(request, 'historia.html', ctx)