from django.shortcuts import render , get_object_or_404
from blog.models import BlogPost
from django.http import Http404

# Create your views here.


def blog_single_views(request,pid):
    try:
        posts = BlogPost.objects.get(id=pid)
        context = {'posts' : posts}
    except BlogPost.DoesNotExist:
            raise Http404("Given query not found....")
    
    
    return render(request , 'blog/blog-single.html' ,context)

def blog_home_views(request):
    posts = BlogPost.objects.all()
    context = {'posts' : posts}
    
    return render(request , 'blog/blog-home.html' ,context)

# def test(request , pid):
#     try:
#         posts = BlogPost.objects.get(id=pid)
#         context = {'posts' : posts}
#     except BlogPost.DoesNotExist:
#             raise Http404("Given query not found....")

    
#     return render(request , 'website/test.html' , context)