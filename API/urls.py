from django.urls import path, include
from API.resources import OrderResource
from API import views
#Creating views for forms

order_resource = OrderResource()

urlpatterns = [
    path('orders/', include(order_resource.urls)),
    path('', views.Home, name='home')
]
