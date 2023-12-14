from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from rest_framework import generics
from rest_framework import views
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    context_object_name = 'products'
    queryset = Product.objects.all()
    # permission_classes = IsAuthenticated

class ProductRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
