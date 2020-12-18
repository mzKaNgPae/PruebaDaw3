"""sitio_webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from usuario import views as usuario_views
from auto import views as auto_views

from django.conf import settings

urlpatterns = [
    path('',core_views.home, name='home'),
    path('about/',core_views.about, name='about'),
    path('contacto/',core_views.contact, name='contacto'),
    path('admin/', admin.site.urls),
    path('login/', usuario_views.login, name='login'),
    path('signup/', usuario_views.signup, name='signup'),
    path('logout/', usuario_views.logout, name='logout'),
    path('tablas-de-records/', auto_views.tablas, name='tablas-de-records'),
    path('historia-fabricantes/', auto_views.historia, name='historia-fabricantes'),
    path('home-admin/', core_views.home_admin, name='home-admin'),
    path('listado-autos/', auto_views.listado_autos, name='listado-autos'),
    path('modificar-auto/<int:pk>/', auto_views.ModificarAutoView.as_view(), name='modificar-auto'),
    path('añadir-auto/', auto_views.CrearAutoView.as_view(), name='añadir-auto'),
    path('', include('pwa.urls')),
    path('save-token/', core_views.guardar_token, name='save-token'),
    path('home-admin/save-token/', core_views.guardar_token, name='admin-save-token')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)