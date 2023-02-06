from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name='user-creation'),
    path('login/<int:id>/<int:token>',Userlogin,name="login_name")
    
]