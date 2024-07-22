from django.shortcuts import render

# Create your views here.


def blog_single_views(request):
    return render(request , 'blog/blog-single.html')

def blog_home_views(request):
    return render(request , 'blog/blog-home.html')