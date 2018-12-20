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


def NewForm(request):
    # Sanity checks
    if not request.user.is_authenticated:
        return HttpResponse("please log in ")
    if not request.method == "POST":
        template = loader.get_template('CreateForm.html')
        context = {"username": request.user.username,
                   "password": request.user.password
                   }
        return HttpResponse(template.render(context, request))
    payload = GetPayload(request)
    # r = requests.post(url = APIurl, data = payload)
    for req in request.POST:
        request.session[str(req)] = request.POST.get(req)
    return redirect('Create/contract')


def EditForm(request, Order_id):
    # Sanity Checks
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    if not request.method == "POST":
        template = loader.get_template('EditForm.html')  # HTML FOR EDIT FORMS
        Order = requests.get(url=APIurl + Order_id + '/',
        data=({'OrderCreator': request.user.username, 'password': request.user.password})).json();
        try:
            context = {"order": Order,
            "Resources": requests.get(url=APIurl + 'Resources/' + Order.get('SystemId') + '/',
                                    data=({'OrderCreator': request.user.username, 'password': request.user.password})).json(),}
            return HttpResponse(template.render(context, request))
        except json.decoder.JSONDecodeError:
            return HttpResponse("Ajja Bajja!")
    r = requests.post(url=APIurl, data=GetPayload(request))
    return redirect('home')


def ViewForms(request):
    # Sanity Check
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    template = loader.get_template('ViewForms.html')  # HTML FOR VIEw forms
    try:
        context = {
            'myOrders': requests.get(url=APIurl + 'User/' + request.user.username + '/',
                                     data=({'OrderCreator': request.user.username, 'password': request.user.password})).json(),
            # 'CurrentUser' : request.user.username,
        }
        return HttpResponse(template.render(context, request))
    except json.decoder.JSONDecodeError:
        return HttpResponse("Ajja Bajja!!!")


def OrderDetail(request, Order_id):
    if not request.user.is_authenticated:
        return HttpResponse("Please log in")
    template = loader.get_template('OrderDetail.html')
    Order = requests.get(url=APIurl + Order_id + '/', data=(
        {'OrderCreator': request.user.username, 'password': request.user.password})).json()
    try:
        context = {
            "order": Order,
            "agreements": requests.get(url=APIurl + Order_id + '/contract/',
                                       data=({'OrderCreator': request.user.username, 'password': request.user.password})).json(),
            "resources": requests.get(url=APIurl + 'Resources/' + Order.get('SystemId', '') + '/',
                                      data=({'OrderCreator': request.user.username, 'password': request.user.password})).json(),
        }
        return HttpResponse(template.render(context, request))
    except json.decoder.JSONDecodeError:
        return HttpResponse("JsonDecodeError")


def ContractPage(request):
    # Sanity Check
    if not request.user.is_authenticated:
        return HttpResponse("Not Valid")
    if not request.method == "POST":
        SystemId = request.session.get('SystemId', '')
        SystemIDcheck = requests.get(
            url=APIurl + 'Exists/Systemid/' + SystemId + '/').json()
        if SystemIDcheck == False:
            return HttpResponse("Invalid system ID")
        template = loader.get_template('ContractPage.html')
        try:
            context = {
                'myOrder':   GetSessionPayload(request),
                'Resources': requests.get(url=APIurl + 'Resources/' + SystemId + '/',
                                          data=({'OrderCreator': request.user.username, 'password': request.user.password})).json()
            }
            return HttpResponse(template.render(context, request))
        except json.decoder.JSONDecodeError:
            return HttpResponse("JSON DECODE ERROR D: ")
    payload = GetPayload(request)
    r = requests.post(url=APIurl, data= {**GetSessionPayload(request), **GetPayload(request)})
    return redirect('home')


def GetSessionPayload(request):
    payload = {}
    payload['OrderName'] = request.session['OrderName']
    payload['SystemId'] = request.session['SystemId']
    payload['Medal'] = request.session['Medal']
    payload['ResponseTime'] = request.session['ResponseTime']
    payload['ServiceTime'] = request.session['ServiceTime']
    print(payload)
    return payload


def GetPayload(request):
    payload = {}
    for req in request.POST:
        payload[str(req)] = request.POST.get(req)
    payload['OrderCreator'] = request.user.username
    payload['password'] = request.user.password
    return payload
