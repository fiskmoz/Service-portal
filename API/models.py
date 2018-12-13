from django.db import models
from django.contrib import auth
from django.utils import timezone
# Create your models here.

# Create your models here.
class Order(models.Model):
    OrderCreator = models.CharField(max_length = 250, default = "NOBODY")
    OrderName = models.CharField(max_length = 250, default = 'defaultordername')
    SystemId = models.CharField(max_length = 250, default = "UNDEFINED")
    Medal = models.CharField(max_length = 250)
    ServiceTime = models.CharField(max_length = 250)
    ResponseTime = models.CharField(max_length = 250)
    Date = models.CharField(max_length = 250, default = timezone.now())
    MostRecent = models.CharField(max_length = 250)
    ParentOrder = models.CharField(max_length = 250, default = "ORIGINAL")

    def __str__(self):
        return self.OrderCreator +': ' + self.OrderName

class Agreements(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    AgreementInText = models.CharField(max_length = 250)

class SystemIdentif(models.Model):
    SystemID = models.CharField(max_length=50, default=None, unique=True)
    Owner = models.CharField(max_length=50, default =None)

    def __str__(self):
        return self.SystemID

class NewResource(models.Model):
    Object = models.CharField(max_length = 50)
    OS = models.CharField(max_length = 50)
    Packet = models.CharField(max_length = 50)
    system = models.ForeignKey(SystemIdentif, to_field='SystemID', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Object
