from django.urls import path
from forms import views

# Creating views for forms

urlpatterns = [
    path('Pending',views.PendingOrders,name = 'pendingorder'),
    path('Create/contract', views.ContractPage, name='contractpage'),
    path('Create', views.NewForm, name='newform'),
    path('<Order_id>/edit', views.EditForm, name='editform'),
    path('<Order_id>', views.OrderDetail, name='orderdetail'),
    path('', views.ViewForms, name='viewform')
]
