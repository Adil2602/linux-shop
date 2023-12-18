from django.shortcuts import render
from django.views.generic import ListView
from ..basket.models import Cart


# Create your views here.
class CartView(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name = 'cart.html'
    queryset = Cart.objects.all()
