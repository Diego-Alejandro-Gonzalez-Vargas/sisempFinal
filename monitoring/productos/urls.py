from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^productos/', views.ProductoList, name='productoList'),
    url(r'^productocreate/$', csrf_exempt(views.ProductoCreate), name='productoCreate'),
    url(r'^productoupdate/$', csrf_exempt(views.ProductoUpdate), name='productoUpdate'),
    url(r'^productodelete/$', csrf_exempt(views.ProductoDelete), name='productoDelete'),
]