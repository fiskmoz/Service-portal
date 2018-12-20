from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from API import views
# Creating views for forms

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('<Order_id>/', views.SpecificOrderView.as_view()),
    path('User/<Username>/',    views.SpecificUsername.as_view()),
    path('Resources/<SystemId>/', views.SpecificResourcesList.as_view()),
    path('Exists/Systemid/<SystemId>/', views.SystemIdExists.as_view()),
    path('<Order_id>/contract/', views.AgreementsList.as_view()),
    path('User/<Username>/<Ordername>/', views.OrderExists.as_view()),
    path('Admin/<Ordernumber>/<status>',views.UpdateStatus.as_view())
    # path('', views.Home, name='home')
]

urlpatterns = format_suffix_patterns(urlpatterns)
