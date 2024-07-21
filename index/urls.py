from django.urls import path
from index.views import *


urlpatterns = [
    path('' , index_views , name="index")
]
