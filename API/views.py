from django.shortcuts import render
from django.http import HttpResponse
from API.models import Order

# Create your views here.
def Home(requests):
    return HttpResponse("You are at API home")

def GetOrder(request, order_id):
    allOrders = Order.objects.all()
    found = "not found"
    for order in allOrders:
        if str(order.id) == order_id:
            currentOrder = order
            found = "found"
            break
    if(found == "not found"):
        return HttpResponse("Order not found")
    return HttpResponse(currentOrder)
