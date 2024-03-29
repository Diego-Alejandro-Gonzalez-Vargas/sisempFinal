from .models import Proveedor
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def ProveedorList(request):
    queryset = Proveedor.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)
@csrf_exempt
def ProveedorCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        proveedor = Proveedor()
        proveedor.name = data_json["name"]
        proveedor.save()
        return HttpResponse("successfully created proveedor")
    
@csrf_exempt
def ProveedorUpdate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        proveedor = Proveedor.objects.get(pk=data_json["id"])
        proveedor.name = data_json["name"]
        proveedor.save()
        return HttpResponse("successfully updated proveedor")
@csrf_exempt 
def ProveedorDelete(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        proveedor = Proveedor.objects.get(pk=data_json["id"])
        proveedor.delete()
        return HttpResponse("successfully deleted proveedor")
    