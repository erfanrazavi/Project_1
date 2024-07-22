from django.shortcuts import render , HttpResponse
from django.http import HttpResponse
# Create your views here.


def index_views(request):
    return render(request , 'website/index.html')

def about_views(request):
    return render(request , 'website/about.html')


def contact_views(request):
    return render(request , 'website/contact.html')

def elements_views(request):
    return render(request , 'website/elements.html')