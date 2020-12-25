from django.shortcuts import render , redirect
from .models import Project ,Service

# Create your views here.

def services_view(request):
    return redirect(request,'/')

def service_list(request,slug):
    projects = Project.objects.filter(service__name = slug)
    services = Service.objects.all()
    return render(request,'services/service_list.htm',{'projects':projects,'services':services,'solutions':solutions})