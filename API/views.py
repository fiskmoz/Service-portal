from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from API.models import Order
from .serializer import OrderSerializer
from rest_framework import generics

# Create your views here.
def Home(requests):
    return HttpResponse("You are at API home")

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all() #filter(OrderCreator = request.user.username)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    def post(self, request):
        OrderCreator = request.user.username
        orderName = request.POST.get('orderName', '')
        Medal = request.POST.get('Medal', '')
        ServiceTime = request.POST.get('ServiceTime', '')
        responseTime = request.POST.get('ResponseTime', '')

        newOrder = Order(OrderCreator=request.user, OrderName=orderName, Date=timezone.now(),
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
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
