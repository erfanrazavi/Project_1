from django.urls import path
from index.views import *
from blog.views import blog_home_views

app_name = 'website'

urlpatterns = [
    path('' , index_views , name="index"),
    path('about/' , about_views , name="about"),
    path('contact/' , contact_views , name="contact"),
    path('category/<str:blog_category>' , blog_home_views , name = 'category'),
    path('newsletter' , news_letter_view , name = 'newsletter'),
    # path('elements/' , elements_views , name="element"),
    
]
