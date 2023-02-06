from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile_no = models.IntegerField(blank=True,null=True)
    user_otp = models.IntegerField(blank=True,default=987651)
    

