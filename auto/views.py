from django.shortcuts import render,redirect
from .models import Auto,Competencia,Imagenes_Marca,Marca
from django.contrib.auth.decorators import login_required
from usuario.validators import usuario_administrador
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CrearAuto,ModificarAuto
from django.views.generic import CreateView,UpdateView
import requests
import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest

from fcm_django.models import FCMDevice

# Create your views here.

@login_required
def tablas(request):
    ctx = {}
    top10 = Auto.objects.all().order_by('-velocidad_maxima')[0:10]
    ctx['top10'] = top10
    competencias = Competencia.objects.all().order_by('nombre','-victorias')
    ctx['competencias'] = competencias

    # CONSUMIR API https://mindicador.cl/ 

    url = 'https://mindicador.cl/api/dolar'
    response = requests.get(url)

    if response.status_code == 200:
        content = json.loads(response.content)
        ctx['valorDolar'] = content['serie'][0]['valor']
    
    # CONSUMIR API https://mindicador.cl/ 

    return render(request, 'tablas.html', ctx)

@login_required
def historia(request):
    ctx = {}
    ctx['i_marcas'] = Imagenes_Marca.objects.all()
    ctx['marcas'] = Marca.objects.all()
    
    return render(request, 'historia.html', ctx)

@login_required
def listado_autos(request):
    if usuario_administrador(request):
        if request.method == 'GET':
            ctx = {}
            autos = Auto.objects.all()
            ctx['l_autos'] = autos
            return render(request, 'adm/listado_autos.html', ctx)
        if request.method == 'POST':
            id_auto = request.POST['id']
            if 'delete' in request.POST:
                Auto.objects.get(id=id_auto).delete()
            if 'edit' in request.POST:
                return redirect('modificar-auto',id_auto)
            return redirect('listado-autos')
        
    return redirect('home')

class CrearAutoView(LoginRequiredMixin,CreateView):
    model = Auto
    template_name = 'adm/crear_auto.html'
    form_class = CrearAuto

    def form_valid(self, form):
        form.save(self.request.user)
        return super(CrearAutoView, self).form_valid(form)
        
    def get_success_url(self, **kwargs):
        nuevo = self.object
        dispositivos = FCMDevice.objects.filter(active=True)
        dispositivos.send_message(
            title='Automovil agregado!!!',
            body='Se ha sumado a nuestra coleccion: ' + str(nuevo.marca) + ' ' + str(nuevo.modelo) + ' \nNo te lo pierdas!!',
            icon='/static/adm/img/cardetail-blanco.png'
        )
        return self.object.get_absolute_url()

class ModificarAutoView(LoginRequiredMixin,UpdateView):
    model = Auto
    template_name = 'adm/modificar_auto.html'
    form_class = ModificarAuto
        
    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()