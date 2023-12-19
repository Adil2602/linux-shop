from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from rest_framework import generics
from rest_framework import views
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class CategoryList(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category_detail'
    queryset = Category.objects.all()


class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    context_object_name = 'products'
    queryset = Product.objects.all()
    # permission_classes = IsAuthenticated


class ProductRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()




class Search(ListView):
    template_name = 'product.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(Q(title__icontains=query) | Q(category__title__icontains=query))
        else:
            return Product.objects.none()  # Возвращаем пустой queryset, так как ничего не найдено

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['q'] = query

        if not context['products']:
            context['no_results'] = True
            context['suggestions'] = Product.objects.values_list('title', flat=True)[:5]  # Подсказки для запроса
        else:
            context['no_results'] = False

        return context
