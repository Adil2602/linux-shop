from django import forms
from ..product.models import Product

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'photo', 'description', 'expiration_date', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'photo', 'description', 'expiration_date', 'category']

