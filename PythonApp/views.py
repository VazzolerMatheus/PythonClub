from django.shortcuts import render
from .models import Resource

# Create your views here.

def index(request) :
   return render(request, 'PythonApp/index.html')


def getResources(request):

	resources_list = Resource.objects.all()

	return render(request, 'PythonApp/resources.html', {'resources_list' : resources_list})
