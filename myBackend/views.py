from django.shortcuts import render
from django.http import HttpResponse

#This is the services vie that handles user request to check services offered.
def services(request):
    return HttpResponse("These are the services offered by AMO parlour")

# Create your views here.
