from django.db import models

NURSERIES = (
    ('Tree Nurseries', 'Tree Nurseries'),
    ('Vegetable Nurseries', 'Vegetable Nurseries'),
    ('Ornmental Nurseries', 'Ornmental Nurseries')
)

PRODUCT_CATEGORIES = (
    ('Plants', 'Plants'),
    ('Equipments', 'Equipments'),
    ('Soil', 'Soil'),
    ('Fertilizers', 'Fertilizers'),
)

class Nurseries(models.Model):
    category = models.CharField(max_length=50, choices= NURSERIES )
    file = models.TextField(max_length=1000)
    def __str__(self):
        return self.category
    
class Plants(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField('Planting day')
    image_url = models.TextField(max_length=500)

    nurseries = models.ForeignKey(Nurseries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField() 
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORIES)
    image_url = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class ProductRequest(models.Model):
    farmer_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_requested = models.PositiveIntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.farmer_name} - {self.product.name}"
