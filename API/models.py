from django.db import models
from django.contrib import auth
# Create your models here.

# Create your models here.
class Order(models.Model):
    OrderCreator = models.CharField(max_length = 250, default = "NOBODY")
    OrderName = models.CharField(max_length = 250, default = 'defaultordername')
    SystemId = models.CharField(max_length = 250, default = "UNDEFINED")
    Medal = models.CharField(max_length = 250)
    ServiceTime = models.CharField(max_length = 250)
    ResponseTime = models.CharField(max_length = 250)
    Date = models.CharField(max_length = 250)
    MostRecent = models.CharField(max_length = 250)
    ParentOrder = models.CharField(max_length = 250, default = "ORIGINAL")


class Agreements(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    AgreementInText = models.CharField(max_length = 250)

class Resources(models.Model):
    Object = models.CharField(max_length = 50)
    OS = models.CharField(max_length = 50)
    Packet = models.CharField(max_length = 50)
    SystemId = models.CharField(max_length = 50)
