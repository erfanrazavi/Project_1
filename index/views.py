from django.shortcuts import render , HttpResponse
from django.http import HttpResponse
# Create your views here.


def index_views(request):
    return render(request , 'index.html')

def about_views(request):
    return render(request , 'about.html')

def blog_views(request):
    return render(request , 'blog.html')

def contact_views(request):
    return render(request , 'contact.html')

def elements_views(request):
    return render(request , 'elements.html')