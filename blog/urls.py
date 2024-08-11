from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed
app_name = 'blog'

urlpatterns = [
    path('<int:pid>' , blog_single_views , name = 'blog-single'),
    path('category/<str:blog_category>' , blog_home_views , name = 'category'),
    path('' , blog_home_views , name = 'blog-home'),
    path('author/<str:username_author>', blog_home_views ,name =  'author'),
    # path('test' , test , name='test'),
    path('search/' , blog_search , name = 'search'),
    path( 'rss/feed/' ,LatestEntriesFeed())
]

