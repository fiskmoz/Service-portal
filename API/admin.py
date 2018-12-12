from django.contrib import admin
from .models import Order
from .models import SystemIdentif, NewResource

# Register your models here.
admin.site.register(Order)
admin.site.register(SystemIdentif)
admin.site.register(NewResource)
