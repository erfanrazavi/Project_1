from django.shortcuts import render , HttpResponse , get_object_or_404 , HttpResponseRedirect
from django.http import HttpResponse , Http404
from .models import Contact
from django.core.paginator import Paginator ,PageNotAnInteger,EmptyPage
from blog.models import BlogPost
from index.forms import ContactForm , NewsLetterForm
from django.contrib import messages


# Create your views here.


def index_views(request):
    posts = BlogPost.objects.filter(status=1)
        
    context = {'posts' : posts}
    return render(request , 'website/index.html' , context)

def about_views(request):
    return render(request , 'website/about.html')


def contact_views(request):
    
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = '*unknown*'
            if not contact.subject:
                contact.subject = ''
            contact.save()
            messages.success(request, 'Dear submission successful' )
        else:
            messages.error(request, 'Dear submission Wrong' )

            
    form = ContactForm()        
        
    return render(request , 'website/contact.html' , {'form' : form})

def news_letter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

    

# def elements_views(request):
#     return render(request , 'website/elements.html')

