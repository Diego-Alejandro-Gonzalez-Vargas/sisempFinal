from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^proveedores/', views.ProveedorList, name='proveedorList'),
    url(r'^proveedorcreate/$', csrf_exempt(views.ProveedorCreate), name='proveedorCreate'),
    url(r'^proveedorupdate/$', csrf_exempt(views.ProveedorUpdate), name='proveedorUpdate'),
    url(r'^proveedordelete/$', csrf_exempt(views.ProveedorDelete), name='proveedorDelete'),
]