from django.shortcuts import render
from .models import Nurseries , Plants
from django.http import HttpResponse


        
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def nurseries_index(request):
    nurseries = Nurseries.objects.all()
    return render(request, 'nurseries/index.html', {'nurseries': nurseries})


def plant_list(request, nurserie_id):
    plants = Plants.objects.all().filter(nurseries=nurserie_id)
    return render(request, 'nurseries/plantlist.html', {'plants': plants})