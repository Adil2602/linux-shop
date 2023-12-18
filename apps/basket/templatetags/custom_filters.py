# your_app/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def total_price(carts):
    total = sum(item.product.price * item.quantity for cart in carts for item in cart.cartitem_set.all())
    return total


@register.filter
def total_items(carts):
    total_items = 0
    for cart in carts:
        total_items += sum(item.quantity for item in cart.cartitem_set.all())
    return total_items
