from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField('Product',max_length=100)
    price = models.CharField('Price', )
    photo = models.ImageField('Photo', upload_to='product/')
    description = models.TextField('Description', blank=True, null=True)
    # expiration_date = models.DateTimeField('Срок годности до', blank=True, null=True)

