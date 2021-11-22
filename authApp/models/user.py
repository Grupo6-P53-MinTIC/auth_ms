from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, email,  password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an Email')

        user = self.model(username=username, email= self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email,  password):
        """
        Creates and saves a superuser with the given username and password.
        """
        if not password:
            raise ValueError('Password should not be none')
        if not email:
            raise ValueError('Users must have an Email')

        user = self.create_user(
            username,
            email ,
            password,
        )
        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15,unique=True,db_index=True )
    email = models.EmailField('Email', max_length = 100, unique=True, db_index=True )
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 30)
    # is_manager = models.BooleanField('Is_manager', default=False)
    # is_verified = models.BooleanField(default=False)
    # is_active =  models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # def save(self, **kwargs):
    #     some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
    #     self.password = make_password(self.password, some_salt)
    #     super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    
    def __str__ (self):
        return self.email
    
    def tokens (self):
        return ''
