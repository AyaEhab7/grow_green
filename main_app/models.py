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

