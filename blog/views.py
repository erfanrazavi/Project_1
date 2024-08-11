from django.shortcuts import render , get_object_or_404 
from blog.models import BlogPost , Comment
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.


def blog_single_views(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dear comment submission successful' )
        else:
            messages.error(request, 'Dear comment submission Wrong' )
   
    
    posts = BlogPost.objects.get(pk=pid , status=1)
    comment = Comment.objects.filter(post=posts.id,approved=True)
    form = CommentForm()
    context = {'posts' : posts , 'comments' : comment , "form" : form}
    
    return render(request , 'blog/blog-single.html' ,context)

def blog_home_views(request,**kwargs):
    posts = BlogPost.objects.filter(status=1)
   
    if kwargs.get('blog_category') != None:
        posts = posts.filter(category__name=kwargs['blog_category'])
   
    if kwargs.get('username_author') != None:
        posts = posts.filter(author__username=kwargs['username_author'])
    
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts.paginator.page(paginator.num_pages)
    
    context = {'posts' : posts}
    
    return render(request , 'blog/blog-home.html' ,context)

def blog_search(request):
    # print(request.__dict__)
    posts = BlogPost.objects.filter(status=1)
    if request.method == 'GET':
        # print(request.GET.get('s'))
        if w_s := request.GET.get('s'):  #python walrus
            posts = posts.filter(content__contains=w_s)
        
    
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' ,context)















# def test(request ):
    
#     return render(request , 'website/test.html')

# def blog_category(request , blog_category):
#     posts = BlogPost.objects.filter(status=1)
#     posts = posts.filter(category__name=blog_category)
#     context = {'posts' : posts}
#     return render(request , 'blog/blog-home.html' ,context)


