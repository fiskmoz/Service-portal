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
        orders = Order.objects.filter(OrderCreator = request.user.username)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    def post(self, request):
        return ("TODO")
        # WHAT TO DO WHEN RECEIVING A POST (NEW ORDER?)

class SpecificOrderView(APIView):
    lookup_field  = 'id'

    # def get_queryset(self):
        # return Order.objects.all()

    def get(self, request, id):
        order = Order.objects.get(id = id)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
