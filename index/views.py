from django.shortcuts import render , HttpResponse
from django.http import HttpResponse
# Create your views here.


def index_views(request):
    return render(request , 'index.html')