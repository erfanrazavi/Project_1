from django.urls import path
from account.views import *


app_name = 'accounts'

urlpatterns = [
    path('login/' , login_views , name="login"),
    # path('login_email/' , login_views , name="login_email"),
    path('logout/' , logout_views , name="logout"),
    path('register/' , register_views , name="register"),
    #logout
    #registration / signup 
    
    
]