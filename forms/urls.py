from django.urls import path
from . import views

#Creating views for forms

urlpatterns = [
    path('Create', views.NewForm, name='newform'),
    path('Edit', views.EditForm, name='editform'),
    path('^(?P<order_id>)/$', views.OrderDetail, name = 'orderdetail'),
    path('', views.ViewForms, name='viewform')
]
