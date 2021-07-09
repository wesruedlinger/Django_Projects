from django.db import models
from django.urls import reverse
from PIL import Image

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Product_Category'
        verbose_name_plural = 'Product_Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:products_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(default='DefaultProductImg.png', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name
    
    @property
    def imgURL(self):
        return self.image.url

    def get_absolute_url(self):
        return reverse('store:product_details', args=[self.id, self.slug])