from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField('Username', max_length=20, unique=True)
    email = models.EmailField('Email', max_length=40, unique=True)
    avatar = models.ImageField('Avatar', upload_to='.media/images/', null=True, blank=True)
    created = models.DateTimeField('Account creation date', auto_now_add=True)

    is_farmer = models.BooleanField(default=False)

    def save_as_farmer(self):
        self.is_farmer = True
        self.save()



class Farmer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserFarmer')
    phone = models.CharField('Phone', max_length=15, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    farm_address = models.CharField(max_length=255, null=True, blank=True)

    card_number = models.CharField(max_length=16, null=True, blank=True)
    card_holder_name = models.CharField(max_length=100, null=True, blank=True)
    expiration_date = models.DateField('expirations date', null=True, blank=True)
    cvv_code = models.CharField(max_length=3, null=True, blank=True)


