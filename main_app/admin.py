from django.contrib import admin
from .models import Nurseries, Plants
from .models import Product, ProductRequest

admin.site.register(Nurseries)
admin.site.register(Plants)
admin.site.register(Product)
admin.site.register(ProductRequest)

