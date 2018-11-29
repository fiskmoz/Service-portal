from django.urls import path
from forms import views

#Creating views for forms

urlpatterns = [
    path('Create/contract', views.ContractPage, name='contractpage'),
    path('Create', views.NewForm, name='newform'),
    path('<order_id>/edit', views.EditForm, name='editform'),
    path('<order_id>', views.OrderDetail, name = 'orderdetail'),
    path('', views.ViewForms, name='viewform')
]
