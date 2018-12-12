from django.contrib import admin
from .models import Order
from .models import SystemIdentif, NewResource

# Register your models here.
# admin.site.register(Order)
# admin.site.register(SystemIdentif)
# admin.site.register(NewResource)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  search_fields = ['OrderCreator', 'OrderName', 'Medal', 'Date']
  list_display = ('OrderCreator', 'OrderName', 'Medal', 'Date')
  list_filter = ('OrderCreator',)

@admin.register(SystemIdentif)
class SystemIdentifAdmin(admin.ModelAdmin):
   search_fields = ['SystemID', 'Owner']
   list_display = ('SystemID', 'Owner')
   list_filter = ('SystemID',)

@admin.register(NewResource)
class NewResourceAdmin(admin.ModelAdmin):
  search_fields = ['system', 'Object', 'OS', 'Packet']
  list_display = ('system', 'Object','OS','Packet')
  list_filter = ('system',)
