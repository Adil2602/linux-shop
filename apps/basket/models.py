from django.db import models
from ..account.models import User
from ..product.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product)
    def __str__(self):
        return f'{self.user} - {self.product} '

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
# 1

