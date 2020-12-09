from django.shortcuts import render,redirect
from .models import Casa,Contacto

# Create your views here.
def main(request):
    return render(request,'home.html',{})

def gallery(request):
    return render(request,'gallery.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        apellidos = request.POST['apellidos']
        telefono = request.POST['telefono']
        Contacto.objects.create(
            nombre = nombre,
            correo = email,
            apellido = apellidos,
            numero = telefono
        )
        return redirect('lista_contact')
    return render(request,'contact.html',{})

def medida(request):
    ctx = {}
    ctx['casa'] = ''
    if request.method == 'GET':
        n_habitaciones = request.GET.get('n_habitaciones')
        n_baños = request.GET.get('n_baños')
        if n_habitaciones and n_baños:
            ctx['casa'] = Casa.objects.filter(habitaciones=int(n_habitaciones),baths=int(n_baños)).first()
    return render(request,'medida.html',ctx)

def metraje(request):
    ctx = {}
    ctx['metros'] = ''
    if request.method == 'GET':
        metros_cuadrados = str(request.GET.get('metros_cuadrados'))
        if metros_cuadrados != 'None':
            lbl_precio = round((float(metros_cuadrados)*33000)/28883.18,2)
        else:
            metros_cuadrados = '0'
            lbl_precio = '0'
   
    return render(request,'metraje.html', {'metros_cuadrados': metros_cuadrados,'lbl_precio': lbl_precio })

def lista_contact(request):
    ctx = {}
    lista_contactos = Contacto.objects.all()
    ctx['lista_contactos'] = lista_contactos
    if request.method == 'POST':
        id_contacto = request.POST['id_contacto']
        Contacto.objects.get(id=id_contacto).delete()
        return redirect('lista_contact')
    return render(request,'lista_contact.html',ctx)