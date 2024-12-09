from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms

from .models import Nurseries , Plants
from .models import Product, ProductRequest

from .forms import ProductRequestForm

@login_required
def product_create(request):
    if not request.user.is_superuser: 
        return redirect('store')
      
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


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'quantity', 'category', 'image_url']
    template_name = 'store/product_form.html'
    success_url = '/store'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'quantity', 'category', 'image_url']
    template_name = 'store/product_form.html'
    success_url = '/store' 

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = '/store'

    def get_success_url(self):
        return reverse_lazy('store') 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image_url']







