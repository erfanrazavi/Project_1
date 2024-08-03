from django.shortcuts import render , HttpResponse , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Contact

# Create your views here.


def index_views(request):
    return render(request , 'website/index.html')

def about_views(request):
    return render(request , 'website/about.html')


def contact_views(request):
    # if request.method == 'POST':
    #     form = Contact(request.POST)
    #     if Contact.is_valid()
    
    return render(request , 'website/contact.html')

# def elements_views(request):
#     return render(request , 'website/elements.html')

