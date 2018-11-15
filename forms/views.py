from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from .models import Order
from django.utils import timezone

# Create your views here.
def NewForm(request):
    if request.user.is_authenticated:
        if request.method == 'POST' :
            service = request.POST.get('button1', '')
            responseTime = request.POST.get('button2', '')
            serviceTime = request.POST.get('button3', '')
            newOrder = Order(User=request.user, Date=timezone.now(),
            Medal=service, ServiceTime=serviceTime, ResponseTime=responseTime)
            newOrder.save()
            return HttpResponse('Success!')
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
