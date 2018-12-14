from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import OrderSerializer
from rest_framework import generics
from django.utils import timezone
from django.template import loader
from API.models import NewResource, SystemIdentif, Agreements, Order
from .serializer import NewResourceSerializer, SystemIdentifSerializer, AgreementsSerializer, OrderSerializer
from django.contrib.auth.models import User

# Create your views here.
def Home(requests):
    return HttpResponse("You are at API home")

class OrderList(APIView):
    #  Get all orders
    def get(self, request):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")

        user = User.objects.get(username = caller)

        if not user.is_superuser == 1:
            return HttpResponse("Not enough privileges")

        orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    # Add a new order
    def post(self, request):
        print("In new order")
        if not Authenticate(request):
            print("not auth")
            return HttpResponse("Not authenticated")
        print("Passed auth")
        OrderName = request.POST.get('OrderName', '')
        OrderCreator = request.POST.get('OrderCreator', '')
        print(OrderName + "    " + OrderCreator)
        if  Order.objects.filter(OrderCreator=OrderCreator).filter(OrderName=OrderName) :
            return HttpResponse("Ordername duplicate")
        CreateNewOrder(request)
        return HttpResponse("SUccess!!!")

    def delete(self,request):
        pass
    def update(self,request):
        pass
    def patch(self,request):
        pass

class SpecificOrderView(APIView):
    lookup_field  = 'OrderName'
    # Get information from specific order
    def get(self, request, OrderName):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")
        order = Order.objects.get(OrderName = OrderName)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    # Update exisiting order

    def post(self, request, OrderName ):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")
        OldOrder = Order.objects.get(OrderName = OrderName)
        OldOrder.MostRecent = "FALSE"
        OldOrder.save()
        NewOrder = CreateNewOrder(request)
        NewOrder.ParentOrder = OrderName
        NewOrder.save()
        return HttpResponse("Sucess!")

    def delete(self,request):
        pass
    def update(self,request):
        pass
    def patch(self,request):
        pass



class SpecificResourcesList(APIView):
    lookup_field = 'SystemId'

    def get(self, request, SystemId):
        if not Authenticate(request):
            return HttpResponse("Not authenticated")
        ResourceList = NewResource.objects.filter(system = SystemId)

        serializer = NewResourceSerializer(ResourceList, many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
    def delete(self,request):
        pass
    def update(self,request):
        pass
    def patch(self,request):
        pass

class OrderExists(APIView):

    def get(self,request,Username,Ordername):


        OrderList = Order.objects.filter(OrderCreator=Username).filter(OrderName=Ordername)
        #serializer = OrderSerializer(OrderList, many=True)
        if not OrderList:
            return Response(False)
        return Response(True)


class AgreementsList(APIView):
    lookup_field = 'OrderName'

    def get(self, request, OrderName):
        OrderList = Agreements.objects.filter(OrderName = OrderName)

        serializer = AgreementsSerializer(OrderList, many=True)
        return Response(serializer.data)

    def post(self,request, OrderName):
        if not Authenticate(request):
            return HttpResponse("Not Authenticated")
        return GenerateAgreements(request)
    def delete(self,request):
        pass
    def update(self,request):
        pass
    def patch(self,request):
        pass

class SystemIdExists(APIView):
    lookup_field = 'SystemId'

    def get(self,request,SystemId):

#        if not Authenticate(request):
#           return HttpResponse("Not authenticated")

        ResourceList = SystemIdentif.objects.filter(SystemID = SystemId)
        serializer = SystemIdentifSerializer(ResourceList, many=True)
        if not ResourceList:
            return Response(False)
        return Response(True)

    def post(self,request):
        pass
    def delete(self,request):
        pass
    def update(self,request):
        pass
    def patch(self,request):
        pass


class SpecificUsername(APIView):
    # Get orders for specific user
    lookup_field = 'Username'

    def get(self,request,Username):

        if not Authenticate(request):
            return HttpResponse("Not authenticated")

        orders = Order.objects.filter(OrderCreator = Username)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
    def delete(self,request):
        pass
    def update(self,request):
        pass
    def patch(self,request):
        pass

def Authenticate(request):
    username = request.POST.get('OrderCreator')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username = username)
        print("user found")
    except User.DoesNotExist:
        return False
    if not user.password == password :
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
    Medal=Medal, ServiceTime=ServiceTime, ResponseTime=responseTime, MostRecent="TRUE")
    newOrder.save()
    return newOrder

def GenerateAgreements(request):
    if not Authenticate(request):
        return HttpResponse("Not Authenticated")
    theOrder = CreateNewOrder(request)
    orderName = request.POST.get('OrderName', '')
    print(request.POST)
    for index, box in enumerate(request.POST):
        if 'OrderCreator' in box :
            break
        if index > 0:
            resourceID = NewResource.objects.get(ResourceID = request.POST.get(box))
            checkBoxType = str(box).replace(request.POST.get(box),'')
            newAgreement = Agreements(ResourceID = resourceID, OrderName = theOrder, CheckBoxType = checkBoxType)
            newAgreement.save()
    return HttpResponse('Order Placed Successfully!')
