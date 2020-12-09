from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
 

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
