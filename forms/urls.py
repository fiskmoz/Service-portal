from django.urls import path
from . import views

#Creating views for forms

urlpatterns = [
    path('Create', views.NewForm, name='newform'),
    path('Edit', views.EditForm, name='editform'),
    path('', views.ViewForms, name='viewform')
]
