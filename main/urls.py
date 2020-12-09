from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('medida', views.medida, name='medida'),
    path('metraje', views.metraje, name='metraje'),
    path('contact', views.contact, name='contact'),
    path('lista_contact', views.lista_contact, name='lista_contact'),
]