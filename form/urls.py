from django.urls import path
from . import views

#Creating views for forms

urlpatterns = [
    path(r'form', views.mainpage),
    path(r'forms', views.mainpage),
]