from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario
from django.contrib.auth.models import User
from usuario.validators import usuario_administrador
import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest

from fcm_django.models import FCMDevice

# Create your views here.

@login_required
@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id=token, active=True)

    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El token ya existe'}))

    dispositivo = FCMDevice()

    dispositivo.registration_id = token
    dispositivo.active = True

    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'Token Guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El token no se ha podido guardar'}))

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def about(request):
    ctx = {}
    admins = Usuario.objects.all().filter(tipo_usuario=1)
    ctx['admins'] = admins
    return render(request, 'core/about.html', ctx)
    
@login_required
def contact(request):
    return render(request, 'core/contacto.html')

@login_required
def home_admin(request):
    if usuario_administrador(request):
        return render(request, 'adm/base.html')
    return redirect('home')


    