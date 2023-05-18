from .models import Pedido
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def PedidoList(request):
    queryset = Pedido.objects.all()
    context = list(queryset.values('id', 'products', 'unidades', 'provider', 'fechaEntrega', 'fechaPedido'))
    return JsonResponse(context, safe=False)

def PedidoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        pedido = Pedido()
        pedido.products = data_json["products"]
        pedido.unidades = data_json["unidades"]
        pedido.provider = data_json["provider"]
        pedido.fechaEntrega = data_json["fechaEntrega"]
        pedido.fechaPedido = data_json["fechaPedido"]
        pedido.save()
        return HttpResponse("successfully created pedido")
    

def PedidoUpdate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        pedido = Pedido.objects.get(pk=data_json["id"])
        pedido.products = data_json["products"]
        pedido.unidades = data_json["unidades"]
        pedido.provider = data_json["provider"]
        pedido.fechaEntrega = data_json["fechaEntrega"]
        pedido.fechaPedido = data_json["fechaPedido"]
        pedido.save()
        return HttpResponse("successfully updated pedido")
    
def PedidoDelete(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        pedido = Pedido.objects.get(pk=data_json["id"])
        pedido.delete()
        return HttpResponse("successfully deleted pedido")
    