from django import forms
from .models import ProductRequest

class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ['quantity_requested']
