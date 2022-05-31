import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin


#from ibmn.users.managers import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True, default=None)
    gender = models.CharField(null=True, max_length=10)
    #is_staff = models.BooleanField(default=True) 

    #@property
    #def is_staff(self):
     #   return self.is_staff

    def __str__(self):
        return f'{self.email}'

   