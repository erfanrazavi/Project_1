from django.urls import path
from index.views import *


urlpatterns = [
    path('' , index_views , name="index"),
    path('about/' , about_views , name="about"),
    path('contact/' , contact_views , name="contact"),
    path('elements/' , elements_views , name="element"),
    path('blog/' , blog_views , name="blog"),
]
