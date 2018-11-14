from django.urls import path
from . import views

#Creating views for forms

urlpatterns = [
    path('', views.NewForm, name='newform'),
]
