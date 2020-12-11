from django.shortcuts import render,redirect
from .models import Auto,Competencia,Imagenes_Marca,Marca
from django.contrib.auth.decorators import login_required
from usuario.validators import usuario_administrador
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CrearAuto,ModificarAuto
from django.views.generic import CreateView,UpdateView
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
        return self.object.get_absolute_url()

class ModificarAutoView(LoginRequiredMixin,UpdateView):
    model = Auto
    template_name = 'adm/modificar_auto.html'
    form_class = ModificarAuto
        
    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()