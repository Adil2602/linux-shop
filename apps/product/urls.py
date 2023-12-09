from django.urls import path

from .views import Product

urlpatterns = [
    path('product/', Product.as_view, name='product')
]
