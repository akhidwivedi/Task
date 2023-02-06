from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from django.http import HttpResponse

def Userlogin(request,id,token):
    if request.method == "GET":
        log_user = get_object_or_404(CustomUser,pk=id)
        if  log_user:
            log_user.user_otp == token
            return HttpResponse("User is logged in  with the  token {} ".format(log_user.user_otp))
    return HttpResponse("please register the User")
    

class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)