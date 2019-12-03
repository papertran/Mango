from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
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
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Creation of custon User class to have userUUID
class userAccount(AbstractBaseUser):
    # Required Fields
    email = models.EmailField(verbose_name='email', max_length=128 , unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Extra Field
    user_id = models.AutoField(primary_key=True)
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

# Account Table
class Account(models.Model):
    account_ID = models.AutoField(primary_key=True)
    account_PlaidID = models.CharField(max_length=128,unique=True, null=True, editable=False)
    account_name = models.CharField(max_length=128)
    account_type = models.CharField(max_length=128)

    # This connects the account to a user, A user can have many accounts
    user = models.ForeignKey(userAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_name + " - " + self.account_type


class Category(models.Model):
    category_ID = models.AutoField(primary_key=True, editable=False)
    category_name = models.CharField(max_length=128, null=False)
    category_color = models.CharField(max_length=11, null=False)

    def __str__(self):
        return self.category_name

class Transactions(models.Model):
    transaction_ID = models.AutoField(primary_key=True, editable=False)
    transaction_plaidID = models.CharField(max_length=128, unique=True, null=True, editable=False)
    transaction_name = models.CharField(max_length=128, null=False)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    transaction_location = models.CharField(max_length=256, editable=True, null=True)
    transaction_date = models.DateField(auto_now=False)

    # The keys that its related to
    account= models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.transaction_name