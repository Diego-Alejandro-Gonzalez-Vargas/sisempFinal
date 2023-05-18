from .models import Producto
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def ProductoList(request):
    queryset = Producto.objects.all()
    context = list(queryset.values('id', 'name', 'unidades', 'price', 'category', 'image'))
    return JsonResponse(context, safe=False)

def ProductoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        producto = Producto()
        producto.name = data_json["name"]
        producto.price = data_json["price"]
        producto.category = data_json["category"]
        producto.image = data_json["image"]
        producto.unidades = data_json["unidades"]
        producto.save()
        return HttpResponse("successfully created producto")
    

def ProductoUpdate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        producto = Producto.objects.get(pk=data_json["id"])
        producto.name = data_json["name"]
        producto.price = data_json["price"]
        producto.category = data_json["category"]
        producto.image = data_json["image"]
        producto.unidades = data_json["unidades"]
        producto.save()
        return HttpResponse("successfully updated producto")
    
def ProductoDelete(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        producto = Producto.objects.get(pk=data_json["id"])
        producto.delete()
        return HttpResponse("successfully deleted producto")
    