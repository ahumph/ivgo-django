from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("IVGO index page")

def about(request):
    return HttpResponse("IVGO about page")
