from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('single' , blog_single_views , name = 'blog-single'),
    path('' , blog_home_views , name = 'blog-home')
]

