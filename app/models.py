from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('SM')
        ne=self.normalize_email(email)#ne=normalize email
        
        UserProfileObject=self.model(email=ne,first_name=first_name,last_name=last_name)
        UserProfileObject.set_password(password)
        UserProfileObject.save()
        return UserProfileObject
          
    def create_superuser(self,email,first_name,last_name,password):
        UserProfileObject=self.create_user(email,first_name,last_name,password)
        UserProfileObject.is_superuser=True
        UserProfileObject.is_staff=True
        UserProfileObject.save()
        return UserProfileObject


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    def __str__(self):
        return self.first_name+" "+self.last_name