from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'display_photo',
        'expiration_date',
        'display_categories',
    ]
    list_filter = ['category']

    def display_photo(self, obj):
        # Display a thumbnail for the 'photo' field
        return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)

    display_photo.short_description = 'Photo'

    def display_categories(self, obj):
        # Display the title of the related category
        return obj.category.title if obj.category else ''

    display_categories.short_description = 'Categories'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'display_photo',
    ]

    def display_photo(self, obj):
        # Display a thumbnail for the 'photo' field
        return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)

    display_photo.short_description = 'Photo'
