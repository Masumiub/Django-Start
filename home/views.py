from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is our Homepage")

def about(request):
    return HttpResponse("This is our About page")

def services(request):
    return HttpResponse("This is our Services page")

def contact(request):
    return HttpResponse("This is our Contact page")