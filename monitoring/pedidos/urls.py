from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^pedidos/', views.PedidoList, name='pedidoList'),
    url(r'^pedidocreate/$', csrf_exempt(views.PedidoCreate), name='pedidoCreate'),
    url(r'^pedidoupdate/$', csrf_exempt(views.PedidoUpdate), name='pedidoUpdate'),
    url(r'^pedidodelete/$', csrf_exempt(views.PedidoDelete), name='pedidoDelete'),
]