from productos.models import Producto
from proveedores.models import Proveedor
from .models import Pedido
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import get_object_or_404
@csrf_exempt
def PedidoList(request):
    queryset = Pedido.objects.all()
    context = list(queryset.values('id', 'products', 'unidades', 'provider', 'fechaEntrega', 'fechaPedido'))
    return JsonResponse(context, safe=False)
@csrf_exempt
def PedidoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        pedido = Pedido()
        pedido.unidades = data_json["unidades"]
        proveedor_id = data_json["provider"]
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        pedido.provider = proveedor
        pedido.fechaEntrega = data_json["fechaEntrega"]
        pedido.fechaPedido = data_json["fechaPedido"]
        pedido.save()
        productos_ids = data_json["products"]
        productos = Producto.objects.filter(id__in=productos_ids)

        # Agregar los productos al pedido utilizando el método set()
        pedido.products.set(productos)
        return HttpResponse("successfully created pedido")
    
@csrf_exempt
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
@csrf_exempt
def PedidoDelete(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        pedido = Pedido.objects.get(pk=data_json["id"])
        pedido.delete()
        return HttpResponse("successfully deleted pedido")
    