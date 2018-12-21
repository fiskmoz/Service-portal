from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.utils import timezone
from django.template import loader
from API.models import NewResource, SystemIdentif, Agreements, Order
from .serializer import NewResourceSerializer, SystemIdentifSerializer, AgreementsSerializer, OrderSerializer
from django.contrib.auth.models import User

# Create your views here.


def Home(requests):
    return HttpResponse("You are at API home")


class UpdateStatus(APIView):

    def post(self,request,Ordernumber,status):

        if not Authenticate(request):
            return HttpResponse("Not authenticated")

        user = User.objects.get(username=request.POST.get('OrderCreator'))
        if not user.is_superuser == 1:
            return HttpResponse("Not enough privileges")

        order = Order.objects.get(pk = Ordernumber)
        print(status)
        if status == "Accept":

            order.Status = 'Active'
            order.save()
            print(order.ParentOrder)
            if not order.ParentOrder == "ORIGINAL":

                oldorder = Order.objects.get(pk = order.ParentOrder)
                oldorder.Status = 'Inactive'
                oldorder.save()
        elif status == "Deny":
            order.Status = 'Inactive'
            order.save()
        return HttpResponse("Success")

class OrderList(APIView):
    #  Get all orders
    def get(self, request):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")

        caller = request.POST.get('OrderCreator')
        user = User.objects.get(username=caller)

        if not user.is_superuser == 1:
            return HttpResponse("Not enough privileges")

        orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    # Add a new order
    def post(self, request):
        GenerateAgreements(request)
        return HttpResponse('Add successfull')

    def delete(self, request):
        pass

    def update(self, request):
        pass

    def patch(self, request):
        pass


class SpecificOrderView(APIView):
    lookup_field = 'id'
    # Get information from specific order

    def get(self, request, Order_id):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")
        order = Order.objects.get(id=Order_id)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    # Update exisiting order

    def post(self, request, Order_id):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")
    #    OldOrder = Order.objects.get(OrderName=OrderName)
    #    OldOrder.MostRecent = "FALSE"
    #    OldOrder.save()
        NewOrder = GenerateAgreements(request)
        NewOrder.ParentOrder = Order_id
        NewOrder.save()
        return HttpResponse("edit successfull!")

    def delete(self, request):
        pass

    def update(self, request):
        pass

    def patch(self, request):
        pass


class SpecificResourcesList(APIView):
    lookup_field = 'SystemId'

    def get(self, request, SystemId):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")
        ResourceList = NewResource.objects.filter(system=SystemId)

        serializer = NewResourceSerializer(ResourceList, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def update(self, request):
        pass

    def patch(self, request):
        pass


class OrderExists(APIView):

    def get(self, request, Username, Ordername):

        OrderList = Order.objects.filter(
            OrderCreator=Username).filter(OrderName=Ordername)
        #serializer = OrderSerializer(OrderList, many=True)
        if not OrderList:
            return Response(False)
        return Response(True)


class AgreementsList(APIView):
    lookup_field = 'Order_id'

    def get(self, request, Order_id):
        OrderList = Agreements.objects.filter(orderID = Order_id)

        serializer = AgreementsSerializer(OrderList, many=True)
        return Response(serializer.data)

    def post(self, request, Order_id):
        pass

    def delete(self, request):
        pass

    def update(self, request):
        pass

    def patch(self, request):
        pass


class SystemIdExists(APIView):
    lookup_field = 'SystemId'

    def get(self, request, SystemId):

        #        if not Authenticate(request):
        #           return HttpResponse("Not authenticated")

        ResourceList = SystemIdentif.objects.filter(SystemID=SystemId)
        serializer = SystemIdentifSerializer(ResourceList, many=True)
        if not ResourceList:
            return Response(False)
        return Response(True)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def update(self, request):
        pass

    def patch(self, request):
        pass


class SpecificUsername(APIView):
    # Get orders for specific user
    lookup_field = 'Username'

    def get(self, request, Username):

        if not Authenticate(request):
            return HttpResponse("Not authenticated")

        orders = Order.objects.filter(OrderCreator=Username)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def update(self, request):
        pass

    def patch(self, request):
        pass


def Authenticate(request):
    username = request.POST.get('OrderCreator')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
        print("user found")
    except User.DoesNotExist:
        return False
    if not user.password == password:
        return False
    print("authenticated")
    return True


def CreateNewOrder(request):
    if not Authenticate(request):
        return HttpResponse("Not authenticated")
    OrderName = request.POST.get('OrderName', '')
    SystemId = request.POST.get('SystemId', '')
    OrderCreator = request.POST.get('OrderCreator', '')
    Medal = request.POST.get('Medal', '')
    ServiceTime = request.POST.get('ServiceTime', '')
    responseTime = request.POST.get('ResponseTime', '')
    Date = timezone.now()
    newOrder = Order(OrderCreator=OrderCreator, OrderName=OrderName,
                     SystemId=SystemId, Date=Date,
                     Medal=Medal, ServiceTime=ServiceTime, ResponseTime=responseTime, Status="Pending")
    newOrder.save()
    return newOrder


def GenerateAgreements(request):
    if not Authenticate(request):
        return HttpResponse("Not Authenticated")
    orderName = request.POST.get('OrderName', '')
    theOrder = CreateNewOrder(request)
    print(request.POST)
    for index, box in enumerate(request.POST):
        if 'OrderCreator' in box:
            break
        if index > 5:
            resourceID = NewResource.objects.get(
            ResourceID=request.POST.get(box))
            checkBoxType = str(box).replace(request.POST.get(box), '')
            newAgreement = Agreements(
                ResourceID=resourceID, orderID=theOrder, CheckBoxType=checkBoxType)
            newAgreement.save()
    return theOrder
