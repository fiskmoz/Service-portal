from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from API.models import Order
from .serializer import OrderSerializer
from rest_framework import generics
from django.utils import timezone
from API.models import Resources
from .serializer import ResourcesSerializer

# Create your views here.
def Home(requests):
    return HttpResponse("You are at API home")

class OrderList(APIView):
    #  Get all your orders
    def get(self, request):
        OrderCreator = request.POST.get('OrderCreator', '')
        orders = Order.objects.filter(OrderCreator = OrderCreator)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    # Add a new order
    def post(self, request):
        OrderName = request.POST.get('OrderName', '')
        OrderCreator = request.POST.get('OrderCreator', '')
        if  Order.objects.filter(OrderCreator=OrderCreator).filter(OrderName=OrderName) :
            return HttpResponse("Ordername duplicate")
        CreateNewOrder(request)
        return HttpResponse("SUccess!!!")

class SpecificOrderView(APIView):
    lookup_field  = 'id'
    # Get information from specific order
    def get(self, request, id):
        order = Order.objects.get(id = id)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    # Update exisiting order
    def post(self, request, id ):
        OldOrder = Order.objects.get(id = id)
        OldOrder.MostRecent = "FALSE"
        OldOrder.save()
        NewOrder = CreateNewOrder(request)
        NewOrder.ParentOrder = id
        NewOrder.save()
        return HttpResponse("Sucess!")


def CreateNewOrder(request):
    OrderName = request.POST.get('OrderName', '')
    SystemId = request.POST.get('SystemId', '')
    OrderCreator = request.POST.get('OrderCreator', '')
    Medal = request.POST.get('Medal', '')
    ServiceTime = request.POST.get('ServiceTime', '')
    responseTime = request.POST.get('ResponseTime', '')
    newOrder = Order(OrderCreator=OrderCreator, OrderName=OrderName, SystemId=SystemId, Date=timezone.now(),
    Medal=Medal, ServiceTime=ServiceTime, ResponseTime=responseTime, MostRecent="TRUE")
    newOrder.save()
    return newOrder

class SpecificResourcesList(APIView):
    lookup_field = 'SystemId'

    def get(self, request, SystemId):
        ResourceList = Resources.objects.get(SystemId = SystemId)
        serializer = ResourcesSerializer(ResourceList, many=False)
        return Response(serializer.data)
