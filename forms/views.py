from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from .models import Order
from django.utils import timezone

# Create your views here.
def NewForm(request):
    if request.user.is_authenticated:
        if request.method == 'POST' :
            orderName = request.POST.get('orderName', '')
            #print(Order.objects.filter(User=request.user).filter(OrderName=orderName))
            if Order.objects.filter(User=request.user).filter(OrderName=orderName) == False:
                service = request.POST.get('service', '')
                responseTime = request.POST.get('response', '')
                serviceTime = request.POST.get('serviceTime', '')
                newOrder = Order(User=request.user, OrderName=orderName, Date=timezone.now(),
                Medal=service, ServiceTime=serviceTime, ResponseTime=responseTime)
                newOrder.save()
                return HttpResponse('Success!')
            else:
                return HttpResponse('Ordername already exists!')
        else:
            template = loader.get_template('CreateForm.html')
            context = {"my_name": "tempname"}
            return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("please log in ")

def EditForm(request):
    if request.user.is_authenticated:
        template = loader.get_template('EditForm.html') ## HTML FOR EDIT FORMS
        context = {"my_name": "tempname"}
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("Please log in ")

def ViewForms(request):
    if request.user.is_authenticated:
        allOrders = Order.objects.all()
        template = loader.get_template('ViewForms.html') ## HTML FOR VIEw forms
        context = {
        'allOrders' : allOrders,
        'CurrentUser' : request.user.username,
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("please log in ")

def OrderDetail(request, order_id):
    if request.user.is_authenticated:
        return HttpResponse(order_id)
    else:
        return HttpResponse("please log in ")
