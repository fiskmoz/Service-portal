from tastypie.resources import ModelResource
from API.models import Order
from tastypie.authorization import Authorization

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        allowed_methods = ['get','post']
        authorization = Authorization()

    def get_object_list(self, request):
        return super(OrderResource, self).get_object_list(request).filter(User=request.user)
