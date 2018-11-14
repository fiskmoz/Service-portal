from django.urls import path
from . import views

#Creating views for forms

urlpatterns = [
    path(r'', views.mainpage),
    path(r'Login', views.mainpage),
]
