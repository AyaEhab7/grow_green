from django.shortcuts import render, redirect
from .models import Nurseries , Plants
from .models import Product, ProductRequest
from .forms import ProductRequestForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
      
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

def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})

def product_request(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product_request = ProductRequest(farmer_name='', 
                                         product=product,
                                         quantity_requested=quantity)
        product_request.save()
        return redirect('store') 
    
    return render(request, 'store/product_request.html', {'product': product})

def product_detail(request, id):
    product = Product.objects.get(id=id)  
    return render(request, 'store/product_detail.html', {'product': product})
