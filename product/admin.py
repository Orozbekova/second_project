from django.contrib import admin

# Register your models here.


from django.contrib import admin

from product.models import *

admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Author)
