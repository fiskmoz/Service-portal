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

def NewForm(request):
    # Sanity checks
    if not request.user.is_authenticated:
        return HttpResponse("please log in ")

    if not request.method == "POST":
        template = loader.get_template('CreateForm.html')
        context = {"my_name": "tempname"}
        return HttpResponse(template.render(context,request))
    OrderCreator = request.user.username
    OrderName = request.POST.get('OrderName', '')
    print(OrderName)
    Medal = request.POST.get('Medal', '')
    ServiceTime = request.POST.get('ServiceTime', '')
    responseTime = request.POST.get('ResponseTime', '')
    payload = ({'OrderCreator': OrderCreator, 'OrderName': OrderName, 'Medal' : Medal,
    'ServiceTime': ServiceTime, 'ResponseTime': responseTime})
    r = requests.post(url = 'http://127.0.0.1:8000/API/',
    data = payload)
    print(json.dumps(payload))
    return redirect('home')
    messages.info(request, 'ordername already exists!')


def EditForm(request, order_id):
    #Sanity Checks
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    order = GetSpecificOrder(order_id)
    if not order.OrderCreator.username == request.user.username:
        return HttpResponse("NOT YOUR FORM! LEAVE! ")
    if not order.MostRecent == "TRUE":
        return HttpResponse("THIS IS NOT THE MOST RECENT THING")
    if not request.method == "POST":
        template = loader.get_template('EditForm.html') ## HTML FOR EDIT FORMS
        context = {"order": order, }
        return HttpResponse(template.render(context,request))

    updatedOrderName = request.POST.get('orderName', '')
    AddToDatabase(request)
    order.MostRecent = "FALSE"
    order.save()
    return redirect('home')

def ViewForms(request):
    #Sanity Check
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")

    template = loader.get_template('ViewForms.html') ## HTML FOR VIEw forms
    context = {
    'myOrders' : requests.get(url='http://127.0.0.1:8000/API/').json(),
    'CurrentUser' : request.user.username,
    }
    return HttpResponse(template.render(context,request))


def OrderDetail(request, order_id):
    if not request.user.is_authenticated:
        return HttpResponse("Please log in")
    order = GetSpecificOrder(order_id)
    if not order.OrderCreator == request.user.username:
        return HttpResponse("NOT YOUR FORM!!!! LEAVE")
    template = loader.get_template('OrderDetail.html')
    context = {
    "order" : order,
    }
    return HttpResponse(template.render(context,request ))

def GetSpecificOrder(order_id):
    allOrders = Order.objects.all()
    found = "not found"
    for order in allOrders:
        if str(order.id) == order_id:
            currentOrder = order
            found = "found"
            break
    if(found == "not found"):
        return HttpResponse("Order not found")
    return currentOrder
