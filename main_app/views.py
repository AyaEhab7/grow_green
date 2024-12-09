from django.shortcuts import render, redirect
from .models import Nurseries , Plants, Irrigation, Fertilization, PestControl
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import IrrigationForm, FertilizationForm, PestControlForm
#from django.http import HttpResponse

from .forms import ProductRequestForm

@login_required
def product_create(request):
    if not request.user.is_superuser: 
        return redirect('store')
      
def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():          
            user = form.save()
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def nurseries_index(request):
    nurseries = Nurseries.objects.all()
    return render(request, 'nurseries/index.html', {'nurseries': nurseries})

def plant_list(request, nurserie_id):
    plants = Plants.objects.all().filter(nurseries=nurserie_id)
    return render(request, 'nurseries/plantlist.html', {'plants': plants})

def plant_detail(request, plant_id):
    plant = Plants.objects.get(id=plant_id)
    irrigation_form = IrrigationForm()
    fertilization_form = FertilizationForm()
    pest_form = PestControlForm()
    return render(request , 'plants/detail.html', {
        'plant' : plant,
        'irrigation_form': irrigation_form,
        'fertilization_form': fertilization_form,
        'pest_form' : pest_form   
    }) 
    
def add_nursery_care(request, plant_id):
    # plant = Plants.objects.all().filter(plant=plant_id)
    plant = Plants.objects.get(id=plant_id)
    irrigation_form = IrrigationForm(request.POST)
    fertilization_form = FertilizationForm(request.POST)
    pest_control_form = PestControlForm(request.POST)
    
    
    if request.method == 'POST':
        # Check if all forms are valid
        if irrigation_form.is_valid() and fertilization_form.is_valid() and pest_control_form.is_valid():
            # Save the irrigation data
            new_irr = irrigation_form.save(commit=False)
            new_irr.plants_id = plant_id
            new_irr.save()

            # Save the fertilization data
            new_fer = fertilization_form.save(commit=False)
            new_fer.plants_id = plant_id
            new_fer.save()

            # Save the pest control data
            new_pest = pest_control_form.save(commit=False)
            new_pest.plants_id = plant_id
            new_pest.save()

            # Redirect to the plant detail page after saving
            return redirect('plant_detail', plant_id=plant_id)
        
        return render(request, 'plants/detail.html', {
        'plant': plant,
        'irrigation_form': irrigation_form,
        'fertilization_form': fertilization_form,
        'pest_form': pest_control_form
    })
class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plants
    fields = '__all__'
    success_url = '/nurseries/{nurseries_id}'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  
    
class PlantUpdate(UpdateView):
    model = Plants
    fields = ['name', 'type', 'description', 'date', 'image_url']
    success_url = '/nurseries/{nurseries_id}'
    
class PlantDelete(DeleteView):
    model = Plants
    success_url = '/nurseries/{nurseries_id}'
    
                  
"""
def add_irrigation(request, plant_id):
    form = IrrigationForm(request.POST)
    if form.is_valid():
        new_irr = form.save(commit=False)
        new_irr.plant_id = plant_id
        new_irr.save()
    
def add_fertilization(request, plant_id):
    form = FertilizationForm(request.POST)
    if form.is_valid():
        new_fer = form.save(commit=False)
        new_fer.plant_id = plant_id
        new_fer.save()
        

def add_pestControl(request, plant_id):
    form = PestControlForm(request.POST)
    if form.is_valid():
        new_pest = form.save(commit=False)
        new_pest.plant_id = plant_id
        new_pest.save()
         
        
    return redirect('plant_detail', plant_id = plant_id )        

"""



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







