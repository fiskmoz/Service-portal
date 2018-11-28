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
<<<<<<< HEAD


=======
>>>>>>> 94e2792f8bb369b5a92d5c9b5cb7ac1c68cea02a

# Create your views here.
def Home(requests):
    return HttpResponse("You are at API home")

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all() #filter(OrderCreator = request.user.username)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    def post(self, request):
        OrderName = request.POST.get('OrderName', '')
        OrderCreator = request.POST.get('OrderCreator', '')
        if  Order.objects.filter(OrderCreator=OrderCreator).filter(OrderName=OrderName) :
            print("DUPLICATE FOUND")
            return HttpResponse("Ordername duplicate")
        print(OrderCreator)
        Medal = request.POST.get('Medal', '')
        ServiceTime = request.POST.get('ServiceTime', '')
        responseTime = request.POST.get('ResponseTime', '')
        newOrder = Order(OrderCreator=OrderCreator, OrderName=OrderName, Date=timezone.now(),
        Medal=Medal, ServiceTime=ServiceTime, ResponseTime=responseTime, MostRecent="TRUE")
        newOrder.save()
        return HttpResponse("SUccess!!!")
        # WHAT TO DO WHEN RECEIVING A POST (NEW ORDER?)

class SpecificOrderView(APIView):
    lookup_field  = 'id'

    # def get_queryset(self):
        # return Order.objects.all()

    def get(self, request, id):
        order = Order.objects.get(id = id)
        if (order.OrderCreator == request.user.username):
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        return HttpResponseNotFound("404 MOFO")
