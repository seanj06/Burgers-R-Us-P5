from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Model for food categories
    """
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Food(models.Model):
    """
    Model for food 
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    is_vegan = models.BooleanField(default=False, null=True, blank=True)
    is_gluten_free = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
