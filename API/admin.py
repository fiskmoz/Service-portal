from django.contrib import admin
from .models import Order
from .models import Resources, SystemIdentif, NewResource

# Register your models here.
admin.site.register(Order)
admin.site.register(Resources)
admin.site.register(SystemIdentif)
admin.site.register(NewResource)
