from django import forms
<<<<<<< HEAD
from .models import Irrigation, Fertilization, PestControl

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
        
"""class CombinedPlantForm(forms.Form):
    # Fields for Irrigation
    irrigation_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={
                'placeholder': 'Select a date & time',
                'type': 'datetime-local',
            }
        ),
        label="Irrigation Date",
        required=True,
    )
    irrigation_status = forms.ChoiceField(
        choices= Irrigation,
        label="Irrigation Status",
        required=True,
    )
    
    # Fields for Fertilization
    fertilization_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={
                'placeholder': 'Select a date & time',
                'type': 'datetime-local',
            }
        ),
        label="Fertilization Date",
        required=True,
    )
    fertilization_status = forms.ChoiceField(
        choices=Fertilization,
        label="Fertilization Status",
        required=True,
    )
    
    # Fields for Pest Control
    pest_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={
                'placeholder': 'Select a date & time',
                'type': 'datetime-local',
            }
        ),
        label="Pest Control Date",
        required=True,
    )
    pest_status = forms.ChoiceField(
        choices=PestControl,
        label="Pest Control Status",
        required=True,
    )        """
=======
from .models import ProductRequest

class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ['quantity_requested']
>>>>>>> main
