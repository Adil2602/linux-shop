from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializers import ProductSerializer
from django.db.models import Q
from ..account.permissions import IsFarmerOrReadOnlyAndAuthenticated

from .forms import ProductAddForm
from .forms import ProductUpdateForm


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


class ProductListApiViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsFarmerOrReadOnlyAndAuthenticated,)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'update_product.html'
    context_object_name = 'product_update'
    queryset = Product.objects.all()
    permission_classes = (IsFarmerOrReadOnlyAndAuthenticated,)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse('profile')
def create_product(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)

            # Устанавливаем пользователя, который создает продукт
            product.user = request.user

            product.save()
            return redirect('product')

    else:
        form = ProductAddForm()

    return render(request, 'create_product.html', {'form': form})


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
            context['suggestions'] = Product.objects.values_list('title', flat=True)[:3]  # Подсказки для запроса
        else:
            context['no_results'] = False

        return context
