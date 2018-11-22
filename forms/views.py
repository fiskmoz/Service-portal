from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from .models import Order
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages

def AddToDatabase(request):

    orderName = request.POST.get('orderName', '')
    service = request.POST.get('service', '')
    responseTime = request.POST.get('response', '')
    serviceTime = request.POST.get('serviceTime', '')

    newOrder = Order(User=request.user, OrderName=orderName, Date=timezone.now(),
    Medal=service, ServiceTime=serviceTime, ResponseTime=responseTime)
    newOrder.save()


# Create your views here.
def NewForm(request):
    if request.user.is_authenticated:
        if request.method == 'POST' :
            orderName = request.POST.get('orderName', '')
            if not Order.objects.filter(User=request.user).filter(OrderName=orderName) :   # checks if user has an order with the ordername
                AddToDatabase(request)
                return redirect('home')
            else:                                                                       # if ordername exists
                messages.info(request, 'ordername already exists!')
                template = loader.get_template('CreateForm.html')
                context = {"my_name": "tempname"}
                return HttpResponse(template.render(context,request))
        else:                                                                           # first time loading into page
            template = loader.get_template('CreateForm.html')
            context = {"my_name": "tempname"}
            return HttpResponse(template.render(context,request))
    else:                                                                               # if not logged in
        return HttpResponse("please log in ")

def EditForm(request, order_id):
    if request.user.is_authenticated:
        template = loader.get_template('EditForm.html') ## HTML FOR EDIT FORMS
        context = {
            'order' : GetSpecificOrder(order_id)
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("Please log in ")

def ViewForms(request):
    if request.user.is_authenticated:
        template = loader.get_template('ViewForms.html') ## HTML FOR VIEw forms
        context = {
        'myOrders' : GetMyOrders(request.user.username),
        'CurrentUser' : request.user.username,
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("please log in ")

def OrderDetail(request, order_id):
    if request.user.is_authenticated:
        template = loader.get_template('OrderDetail.html')
        context = {
            'order' : GetSpecificOrder(order_id)
        }
        return HttpResponse(template.render(context,request ))
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
