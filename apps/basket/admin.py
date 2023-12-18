from django.contrib import admin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from ..basket.models import Cart, CartItem
from django.db.models import F
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1  # Количество дополнительных полей для отображения

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'item_count',
        'total_price',
    ]
    inlines = [CartItemInline]

    def item_count(self, obj):
        
        return obj.cartitem_set.aggregate(Sum('quantity'))['quantity__sum']
    item_count.short_description = 'Item Count'

    def total_price(self, obj):
        return obj.cartitem_set.aggregate(
            total_price=Coalesce(Sum(F('quantity') * F('product__price')), 0)
        )['total_price']

    total_price.short_description = 'Total Price'


