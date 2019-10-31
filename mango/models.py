from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

# Create your models here.

# Used to manage BaseUserManager
class userAccountManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not password:
            raise ValueError("Users must have an password")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.set_password(password)
        user.save(user=self._db)
        return user 
    
    def create_superuser(self, email, username, password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Creation of custon User class to have userUUID
class userAccount(AbstractBaseUser):
    # Required Fields
    email = models.EmailField(verbose_name='email',max_length="128", unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Extra Field
    userUUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = userAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True