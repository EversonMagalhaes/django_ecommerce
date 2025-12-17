from django.db import models
from products.models import Product # Mantenha APENAS esta importação
from unidecode import unidecode

class Tag(models.Model):
    title = models.CharField(unique=True, max_length=120)
    slug = models.SlugField(unique=True, blank=True) # Melhorar: unique=True
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title
    
    def clean_title(self):
        return unidecode(self.title.strip()).lower()