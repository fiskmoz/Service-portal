from django.db import models
from django.contrib import auth

# Create your models here.
class Order(models.Model):
    User = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    Medal = models.CharField(max_length = 250)
    ServiecTime = models.CharField(max_length = 250)
    ResponseTime = models.CharField(max_length = 250)
    Date = models.CharField(max_length = 250)
    MostRecent = models.CharField(max_length = 250)
    ParentOrder = models.CharField(max_length = 250)
