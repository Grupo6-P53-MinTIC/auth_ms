from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from datetime import datetime


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user (
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User (AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 100, unique=True)
    email = models.EmailField('Email', max_length = 100)
    password = models.CharField('Password', max_length = 100)
    # Personal information 
    name = models.CharField('name', max_length=60, null=False, default='')
    lastName = models.CharField(max_length=60, null=True)
    birthDate = models.DateField(default = datetime.now)
    gender = models.CharField(max_length=40, null=True, choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ))
    documentNumber = models.CharField(max_length=20, null=True)
    phoneNumber = models.CharField (max_length=60, null=True )
    # Driver or passenger
    typeAccount = models.CharField('Type Account', null=False, max_length=60, choices=(
        ('D', 'Driver'),
        ('P', 'Passenger')
    ))
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    # __________________________________________________________________________
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'