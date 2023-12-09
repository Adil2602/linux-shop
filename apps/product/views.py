from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    expiration_date = models.DateField('Срок годности до')