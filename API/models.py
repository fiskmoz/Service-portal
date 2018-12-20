from django.db import models
from django.contrib import auth
from django.utils import timezone
# Create your models here.

# Create your models here.


class Order(models.Model):
    OrderCreator = models.CharField(max_length=250, default="NOBODY")
    OrderName = models.CharField(max_length=250)
    SystemId = models.CharField(max_length=250, default="UNDEFINED")
    Medal = models.CharField(max_length=250)
    ServiceTime = models.CharField(max_length=250)
    ResponseTime = models.CharField(max_length=250)
    Date = models.CharField(max_length=250, default=timezone.now())
    Status = models.CharField(max_length=250)
    ParentOrder = models.CharField(max_length=250, default="ORIGINAL")

    def __str__(self):
        return str(self.id)


class SystemIdentif(models.Model):
    SystemID = models.CharField(max_length=50, default=None, unique=True)
    Owner = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.SystemID


class NewResource(models.Model):
    Object = models.CharField(max_length=50)
    OS = models.CharField(max_length=50)
    Packet = models.CharField(max_length=50)
    ResourceID = models.CharField(
        max_length=50, default=None, unique=True, null=True, blank=True)
    system = models.ForeignKey(
        SystemIdentif, to_field='SystemID', on_delete=models.CASCADE, default=None)

    # def __str__(self):
    #     return self.ResourceID


class Agreements(models.Model):
    ResourceID = models.ForeignKey(
        NewResource, to_field='ResourceID', on_delete=models.CASCADE, default=None)
    orderID = models.ForeignKey(
        Order, on_delete=models.CASCADE, default=None)
    CheckBoxType = models.CharField(max_length=250)
