from django import forms
from .models import Nurseries, Plants, Irrigation, Fertilization, PestControl , Status
from .models import ProductRequest

class IrrigationForm(forms.ModelForm):
    class Meta:            
        model = Irrigation
        fields = ['date', 'irrStatus']
        labels = {
        'date': 'Irrigation Time',
        'irrStatus': 'Irrigation Status',
        }
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local',
                }    
            )
        
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
        
class FertilizationForm(forms.ModelForm):
    class Meta:
        model = Fertilization
        fields = ['date', 'ferStatus']
        labels = {
        'date': 'Fertilization Time',
        'ferStatus': 'Fertilization Status',
        }
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
                
            )
        }    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'    
        
class PestControlForm(forms.ModelForm):
    class Meta:
        model = PestControl
        fields = ['date', 'pestStatus']
        labels = {
        'date': 'Pest Control Time',
        'pestStatus': 'Pest Control Status',
        }
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
                
            )
        } 
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'         
        
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['date', 'note', 'plant_status']
        widgets = {
            'date': forms.DateTimeInput(
                format = ('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }   
            )
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
        

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
        
        