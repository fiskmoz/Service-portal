from django.urls import path
from . import views

#Creating views for forms

urlpatterns = [
    path('Create', views.NewForm, name='newform'),
    path('Edit', views.EditForm, name='editform'),
    path(r'^(?P<order_id>[0-9]+)/$', views.OrderDetail, name = 'orderdetail'),
    path('', views.ViewForms, name='viewform')
]
