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

def AddToDatabase(request):

    orderName = request.POST.get('orderName', '')
    service = request.POST.get('service', '')
    responseTime = request.POST.get('response', '')
    serviceTime = request.POST.get('serviceTime', '')

    newOrder = Order(User=request.user, OrderName=orderName, Date=timezone.now(),
    Medal=service, ServiceTime=serviceTime, ResponseTime=responseTime, MostRecent="TRUE")
    newOrder.save()


def NewForm(request):
    # Sanity checks
    if not request.user.is_authenticated:
        return HttpResponse("please log in ")

    if  request.method == "POST":
        orderName = request.POST.get('orderName', '')
        if not Order.objects.filter(User=request.user).filter(OrderName=orderName) :   # checks if user has an order with the ordername
            AddToDatabase(request)
            return redirect('home')
        messages.info(request, 'ordername already exists!')

    template = loader.get_template('CreateForm.html')
    context = {"my_name": "tempname"}
    return HttpResponse(template.render(context,request))


def EditForm(request, order_id):
    #Sanity Checks
    if not request.user.is_authenticated:
        return HttpResponse("Please log in ")
    order = GetSpecificOrder(order_id)
    if not order.User.username == request.user.username:
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
    'myOrders' : GetMyOrders(request.user.username),
    'CurrentUser' : request.user.username,
    }
    return HttpResponse(template.render(context,request))


def OrderDetail(request, order_id):
    order = GetSpecificOrder(order_id)
    if request.user.is_authenticated:
        if order.User.username == request.user.username:
            template = loader.get_template('OrderDetail.html')
            context = {
            "order" : order,
            }
            return HttpResponse(template.render(context,request ))
        else:
            return HttpResponse("NOT YOUR FORM!!!! LEAVE")
    else:
        return HttpResponse("please log in ")


def GetMyOrders(username):
    allOrders = Order.objects.all()
    myOrders = []
    for order in allOrders:
        if(order.User.username == username):
            myOrders.append(order)
    return myOrders

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
