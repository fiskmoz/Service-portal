from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from API.models import Order
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from API.models import Order
import requests
import json

APIurl = 'http://127.0.0.1:8000/API/'

def GetPayload(request):
    OrderCreator = request.user.username
    OrderName = request.POST.get('OrderName', '')
    SystemId = request.POST.get('SystemId', '')
    Medal = request.POST.get('Medal', '')
    ServiceTime = request.POST.get('ServiceTime', '')
    responseTime = request.POST.get('ResponseTime', '')
    payload = ({'OrderCreator': OrderCreator, 'OrderName': OrderName,
    'SystemId' : SystemId, 'Medal' : Medal,
    'ServiceTime': ServiceTime, 'ResponseTime': responseTime})
    return payload

def NewForm(request):
    # Sanity checks
    if not request.user.is_authenticated:
        return HttpResponse("please log in ")
    if not request.method == "POST":
        template = loader.get_template('CreateForm.html')
        context = {"my_name": "tempname"}
        return HttpResponse(template.render(context,request))
    r = requests.post(url = APIurl, data = GetPayload(request))
    return ContractPage(request)

def EditForm(request, order_id):
    #Sanity Checks
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    if not request.method == "POST":
        template = loader.get_template('EditForm.html') ## HTML FOR EDIT FORMS
        context = {"order": requests.get(url=APIurl+order_id+'/').json(), }
        return HttpResponse(template.render(context,request))
    r = requests.post(url = APIurl+order_id+'/', data = GetPayload(request))
    return redirect('home')

def ViewForms(request):
    #Sanity Check
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    template = loader.get_template('ViewForms.html') ## HTML FOR VIEw forms
    context = {
    'myOrders' : requests.get(url=APIurl).json(),
    'CurrentUser' : request.user.username,
    }
    return HttpResponse(template.render(context,request))

def OrderDetail(request, order_id):
    if not request.user.is_authenticated:
        return HttpResponse("Please log in")
    template = loader.get_template('OrderDetail.html')
    context = {
    "order" : requests.get(url=APIurl+order_id+'/').json(),
    }
    return HttpResponse(template.render(context,request ))

def ContractPage(request):
    #Sanity Check
    if not request.user.is_authenticated:
        return HttpResponse("Not Valid")
    template = loader.get_template('ContractPage.html') # HTML for contractpage
    # Add whats required for the contractpage
    context = GetPayload(request)
    return HttpResponse(template.render(context,request ))
