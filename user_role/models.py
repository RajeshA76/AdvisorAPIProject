from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields import BooleanField, DateTimeField
import jwt
from django.conf import settings
from datetime import datetime, timedelta
import uuid
from django.utils import timezone

from admin_role.models import AdvisorModel



class UserManager(BaseUserManager):

    def create_user(self,username,email,password=None):

        if username is None:
            raise TypeError('users should have a username')

        if email is None:
            raise TypeError('users should have an email')

        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self,username,email,password):
        if password is None:
            raise TypeError("Password should not be none")

        user=self.create_user(username,email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255,unique=True,db_index=True)
    email = models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        token = jwt.encode({'username':self.username,'email':self.email,'exp': datetime.utcnow() + timedelta(hours=24)},settings.SECRET_KEY,algorithm='HS256')
        return token




class Booking(models.Model):
    BookingId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    BookingTime = models.CharField(max_length=100)
    uid = models.ForeignKey(User,on_delete=CASCADE)
    advisor_id = models.ForeignKey(AdvisorModel,on_delete=CASCADE)


    


