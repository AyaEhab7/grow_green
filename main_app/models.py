from django.db import models

NURSERIES = (
    ('Tree Nurseries', 'Tree Nurseries'),
    ('Vegetable Nurseries', 'Vegetable Nurseries'),
    ('Ornmental Nurseries', 'Ornmental Nurseries')
)

IRRIGATION = (
    ('Irrigated', 'Irrigated'),
    ('Needs Irrigation', 'Needs Irrigation'),
    ('Overwatered','Overwatered' ),
    ('Not Watered', 'Not Watered'),
    ('Irrigation Delayed', 'Irrigation Delayed')
)
PRODUCT_CATEGORIES = (
    ('Plants', 'Plants'),
    ('Equipments', 'Equipments'),
    ('Soil', 'Soil'),
    ('Fertilizers', 'Fertilizers'),
)

FRETILIZATION = (
    ('Fertilized', 'Fertilized'),
    ('Needs Fertilization', 'Needs Fertilization'),
    ('Over-Fertilized', 'Over-Fertilized'),
    ('Not Fertilized', 'Not Fertilized'),
    ('Inappropriate Fertilizer', 'Inappropriate Fertilizer')  
)

PEST_CONTROL = (
    ('No Pests', 'No Pests'),
    ('Pest Control Applied', 'Pest Control Applied'),
    ('Few Pests', 'Few Pests'),
    ('Severe Pest Infestation', 'Severe Pest Infestation'),
    ('Recurring Pest Issue', 'Recurring Pest Issue'),
    ('Unknown Pest Type', 'Unknown Pest Type')
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
<<<<<<< HEAD
    
class Irrigation(models.Model):
     date = models.DateTimeField("Irrigation Time")
     irrStatus = models.CharField(
         max_length=50,
         choices=IRRIGATION
     )
     
     plants = models.ForeignKey(Plants, on_delete=models.CASCADE)         
    
     def __str__(self):
        return f"{self.get_irrStatus_display()} on {self.date}"
    
     class Meta:
         ordering = ['-date']
         

class Fertilization(models.Model):
     date = models.DateTimeField("Fertilization Time")
     ferStatus = models.CharField(
         max_length=50,
         choices=FRETILIZATION
     )
     
     plants = models.ForeignKey(Plants, on_delete=models.CASCADE)         
    
     def __str__(self):
        return f"{self.get_ferStatus_display()} on {self.date}"
    
     class Meta:
         ordering = ['-date']     
       
class PestControl(models.Model):
     date = models.DateTimeField("Pest Control")
     pestStatus = models.CharField(
         max_length=50,
         choices=PEST_CONTROL
     )
     
     plants = models.ForeignKey(Plants, on_delete=models.CASCADE)         
    
     def __str__(self):
        return f"{self.get_pestStatus_display()} on {self.date}"
    
     class Meta:
         ordering = ['-date']     
                
        
=======

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
>>>>>>> main
