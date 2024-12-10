from django import forms
from .models import Nurseries, Plants, Irrigation, Fertilization, PestControl , Status
from .models import ProductRequest, Product

class IrrigationForm(forms.ModelForm):
    class Meta:
        model = Irrigation
        fields = ['date', 'irrStatus']
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
                
            )
        }
        
class FertilizationForm(forms.ModelForm):
    class Meta:
        model = Fertilization
        fields = ['date', 'ferStatus']
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
                
            )
        }        
        
class PestControlForm(forms.ModelForm):
    class Meta:
        model = PestControl
        fields = ['date', 'pestStatus']
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
                
            )
        }          
        
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['date', 'note', 'color', 'plant_status']
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }   
            )
        }
        

class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ['quantity_requested']

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = ['name', 'type', 'description', 'date', 'image_url', 'nurseries']
        nurseries = forms.ModelChoiceField(queryset= Nurseries.objects.all(),empty_label="Select Nurserie")
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
                
            )
        }
        