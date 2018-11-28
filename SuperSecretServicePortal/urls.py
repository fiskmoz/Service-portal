from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('forms/', include('forms.urls')),
    path('API/', include('API.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]
