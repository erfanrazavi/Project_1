from django.shortcuts import render , HttpResponse , get_object_or_404 
from django.http import HttpResponse , Http404
from .models import Contact
from django.core.paginator import Paginator ,PageNotAnInteger,EmptyPage
from blog.models import BlogPost
from index.forms import ContactForm
from django.contrib import messages


# Create your views here.


def index_views(request):
    posts = BlogPost.objects.filter(status=1)
    paginator = Paginator(posts , 3)
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts.paginator.page(paginator.num_pages)
        
    context = {'posts' : posts}
    return render(request , 'website/index.html' , context)

def about_views(request):
    return render(request , 'website/about.html')


def contact_views(request):
    form = ContactForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, 'Dear %s! submission successful' % name)
            print('done')
            
        
    return render(request , 'website/contact.html' , {'form' : form})

# def elements_views(request):
#     return render(request , 'website/elements.html')

