from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Usuario,TipoUsuario
 

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_user = request.POST.get('remember', False)

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            if not remember_user:
                request.session.set_expiry(0)
            if user.usuario.tipo_usuario.id == 2:
                return redirect('home')
            else:
                return redirect('about')
        else:
            return redirect('login')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:    
            return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        # Crear usuario
        new_user, created = User.objects.get_or_create(
            username=request.POST['username'],
            email=request.POST['correo']
        )
        if created:
            new_user.set_password(raw_password = request.POST['password'])
            new_user.save()
            rut = request.POST['rut'].split('-')
            dv = rut[1]
            rut = rut[0]
            tipo_usuario = TipoUsuario.objects.get(id=2)
            new_cliente = Usuario.objects.create(
                usuario=new_user,
                rut=rut,
                dv=dv,
                nombres=request.POST['nombres'],
                apellido_paterno=request.POST['ape_pa'],
                apellido_materno=request.POST['ape_ma'],
                telefono=request.POST['telefono'],
                correo=request.POST['correo'],
                tipo_usuario=tipo_usuario
            )
            
            auth.login(request, new_user)
            return redirect('home')
    return render(request, 'signup.html')
