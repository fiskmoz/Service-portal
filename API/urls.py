from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from API import views
#Creating views for forms

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('<id>/', views.SpecificOrderView.as_view()),
    path('User/<Username>/',    views.SpecificUsername.as_view()),
    path('Resources/<SystemId>/', views.SpecificResourcesList.as_view())
    # path('', views.Home, name='home')
]

urlpatterns = format_suffix_patterns(urlpatterns)
