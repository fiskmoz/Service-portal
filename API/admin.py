from django.contrib import admin
from .models import Order
from .models import Resources

# Register your models here.
admin.site.register(Order)
admin.site.register(Resources)
