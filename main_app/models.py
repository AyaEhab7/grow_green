from django.db import models

NURSERIES = (
    ('Tree Nurseries', 'Tree Nurseries'),
    ('Vegetable Nurseries', 'Vegetable Nurseries'),
    ('Ornmental Nurseries', 'Ornmental Nurseries')
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
    