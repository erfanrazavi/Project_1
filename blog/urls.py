from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog-single/' , blog_single_views , name = 'blog-single')
    path('blog-home/' , blog_home_views , name = 'blog-home')
]

