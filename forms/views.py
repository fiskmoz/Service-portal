from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from API.models import Order
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
import requests
import json

APIurl = 'http://127.0.0.1:8000/API/'

def GetPayload(request):
    payload = {}
    for req in request.POST:
        payload[str(req)] = request.POST.get(req)
    payload['OrderCreator'] =  request.user.username
    payload['password'] = request.user.password
    return payload

def NewForm(request):
    # Sanity checks
    if not request.user.is_authenticated:
        return HttpResponse("please log in ")
    if not request.method == "POST":
        template = loader.get_template('CreateForm.html')
        context = {"username" : request.user.username,
        "password" : request.user.password
        }
        return HttpResponse(template.render(context,request))
    r = requests.post(url = APIurl, data = GetPayload(request))
    return ContractPage(request)

def EditForm(request, order_id):
    #Sanity Checks
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    if not request.method == "POST":
        template = loader.get_template('EditForm.html') ## HTML FOR EDIT FORMS
        try:
            context = {"order": requests.get(url=APIurl+order_id+'/',
            data =  ({'OrderCreator' : request.user.username , 'password': request.user.password})).json(), }
            return HttpResponse(template.render(context,request))
        except json.decoder.JSONDecodeError:
            return HttpResponse("Ajja Bajja!")
    print('skickar')
    r = requests.post(url = APIurl + order_id +'/', data = GetPayload(request))
    print(r)
    return redirect('home')

def ViewForms(request):
    #Sanity Check
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    template = loader.get_template('ViewForms.html') ## HTML FOR VIEw forms
    try:
        context = {
        'myOrders' : requests.get(url=APIurl + 'User/'+ request.user.username + '/' ,
        data = ({'OrderCreator' : request.user.username, 'password' : request.user.password})).json(),
        #'CurrentUser' : request.user.username,
        }
        return HttpResponse(template.render(context,request))
    except json.decoder.JSONDecodeError:
        return HttpResponse("Ajja Bajja!!!")

def OrderDetail(request, order_id):
    if not request.user.is_authenticated:
        return HttpResponse("Please log in")
    template = loader.get_template('OrderDetail.html')
    try:
        context = {
        "order" : requests.get(url=APIurl+order_id+'/',
        data =  ({'OrderCreator' : request.user.username , 'password': request.user.password})).json(),
        }
        return HttpResponse(template.render(context,request ))
    except json.decoder.JSONDecodeError:
        return HttpResponse("Ajja Bajja!")

def ContractPage(request):
    #Sanity Check
    if not request.user.is_authenticated:
        return HttpResponse("Not Valid")
    template = loader.get_template('ContractPage.html') # HTML for contractpage
    # Add whats required for the contractpage
    SystemId = request.POST.get('SystemId', '')
    SystemIDcheck = requests.get(url=APIurl+'Exists/Systemid/'+SystemId+'/').json()

    if SystemIDcheck == False:
        return HttpResponse("Ajja Bajja3!")
    try:
        context = {
        'myOrder' : GetPayload(request),
        'Resources' : requests.get(url=APIurl+'Resources/'+SystemId+'/',
        data =  ({'OrderCreator' : request.user.username , 'password': request.user.password})).json()
        }
        return HttpResponse(template.render(context, request ))
    except json.decoder.JSONDecodeError:
        return HttpResponse("Ajja Bajja2!")
