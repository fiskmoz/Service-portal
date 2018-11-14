from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def NewForm(request):
    if request.user.is_authenticated:
        template = loader.get_template('FormHome.html')
        context = {"my_name": "tempname"}
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("please log in ")
