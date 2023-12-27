from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# class SellerManager(BaseUserManager):
#     def create_seller(self, email=None, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         seller = self.model(email=email, **extra_fields)
#         seller.set_password(password)
#         seller.save()
#         return seller
#
# class Seller(AbstractUser):
#     username = models.CharField('Username', max_length=20, unique=True)
#     email = models.EmailField('Email', max_length=40, unique=True)
#     avatar = models.ImageField('Avatar', upload_to='media/images/', null=True, blank=True)
#     created = models.DateTimeField('Account creation date', auto_now_add=True)
#
#     objects = SellerManager()
#
#     def __str__(self):
#         return self.username
