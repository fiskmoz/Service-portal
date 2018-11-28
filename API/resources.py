from tastypie.resources import ModelResource
from API.models import Order

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
