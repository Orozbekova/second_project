from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=30,primary_key=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.slug


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    author = models.CharField(max_length=30,default='')

    def __str__(self):
        return self.name


