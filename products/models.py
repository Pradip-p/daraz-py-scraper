from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    rating = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=200, null=True)
    sold_by = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=True)
    productUrl = models.URLField()
    
    def __str__(self):
        return self.name
