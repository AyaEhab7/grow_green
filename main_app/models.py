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
    image_url = models.TextField(max_length=1000)

    nurseries = models.ForeignKey(Nurseries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
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
                
        