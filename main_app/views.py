from django.shortcuts import render,get_object_or_404, redirect
from .models import Nurseries , Plants, Product, ProductRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import IrrigationForm, FertilizationForm, PestControlForm , StatusForm , PlantForm
from django import forms
from django.urls import reverse_lazy
from .models import ProductRequest
from .models import UserProfile


@login_required
def product_create(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if not request.user.is_superuser: 
        return redirect('store', {'role': user_profile.role})
      
class Home(LoginView):
    template_name = 'home.html'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():          
            user = form.save()
            login(request, user)
            return redirect('nurseries-index')
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
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'nurseries/index.html', {'nurseries': nurseries,'role': user_profile.role})

@login_required
def plant_list(request, nurserie_id):
    plants = Plants.objects.all().filter(nurseries=nurserie_id)
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'nurseries/plantlist.html', {'plants': plants,'role': user_profile.role})

@login_required
def plant_detail(request, plant_id):
    plant = Plants.objects.get(id=plant_id)
    irrigation_form = IrrigationForm()
    fertilization_form = FertilizationForm()
    pest_form = PestControlForm()
    status_form = StatusForm()
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request , 'plants/detail.html', {
        'plant' : plant,
        'role': user_profile.role,
        'irrigation_form': irrigation_form,
        'fertilization_form': fertilization_form,
        'pest_form' : pest_form,
        'status_form' : status_form 
    }) 

@login_required
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
    
class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plants
    success_url = '/nurseries/{nurseries_id}'

@login_required
def store(request):
    products = Product.objects.all()
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'store/store.html', {
        'products': products,
        'role': user_profile.role})


@login_required
def product_detail(request, id):
    product = Product.objects.get(id=id)  
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'store/product_detail.html', {
        'product': product, 
        'role': user_profile.role
        })


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'quantity', 'category', 'image_url']
    template_name = 'store/product_form.html'
    success_url = '/store'
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Automatically set the user to the current logged-in user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'quantity', 'category', 'image_url']
    template_name = 'store/product_form.html'
    success_url = '/store' 

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = '/store'

    def get_success_url(self):
        return reverse_lazy('store') 

@login_required
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image_url']

def product_request_detail(request, product_request_id):
    product_request = get_object_or_404(ProductRequest, id=product_request_id)    
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'store/request/product_request_detail.html', {
        'product_request': product_request, 
        'role': user_profile.role})

class ProductRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductRequest
    fields = ['product', 'quantity_requested']
    template_name = 'store/request/product_request_form.html'

    def get_object(self, queryset=None):
        return ProductRequest.objects.get(id=self.kwargs['product_request_id'])

    def get_success_url(self):
        return reverse_lazy('store')

class ProductRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductRequest
    template_name = 'store/request/product_request_confirm_delete.html'
    
    def get_object(self, queryset=None):
        return ProductRequest.objects.get(id=self.kwargs['product_request_id'])

    def get_success_url(self):
        return reverse_lazy('store')  
     
class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ['farmer_name', 'product', 'quantity_requested']


def product_request(request, product_id):
    product = Product.objects.get(id=product_id)
    product_requests = ProductRequest.objects.filter(product=product)
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        farmer_name = request.POST.get('farmer_name')
        status = request.POST.get('status')

        product_request = ProductRequest(
            farmer_name=farmer_name,
            product=product,
            quantity_requested=quantity,
            status=status
        )
        product_request.save()
        return redirect('store')  

    return render(request, 'store/product_request.html', {
        'product': product,
        'product_requests': product_requests,
        'role': user_profile.role  
    })

@login_required
def add_status(request, plant_id):
    plant = Plants.objects.get(id=plant_id)
    status_form = StatusForm(request.POST)
    
    if request.method == 'POST':
        if status_form.is_valid():
            new_status = status_form.save(commit=False)
            new_status.plants_id = plant_id
            new_status.save()
            user_profile = UserProfile.objects.get(user=request.user)
            return redirect('plant_detail', plant_id=plant_id)
        
        return render(request, 'plants/detail.html', {
        'plant': plant,
        'status_form': status_form,
        'role': user_profile.role
    })

@login_required
def add_plant(request):
    
    if request.method == 'POST':
        plant_form = PlantForm(request.POST)
        if plant_form.is_valid():
            new_plant = plant_form.save(commit=False)
            new_plant.user_id = request.user.id
            new_plant.save()

            return redirect('nurseries-index')
        
    plant_form = PlantForm()
    return render(request, 'main_app/plants_form.html', {
        'plant_form': plant_form,
        
    })
        
@login_required
def edit_plant(request, pk):
    plant = get_object_or_404(Plants, pk=pk)

    #if plant.user_id != request.user.id:
        #return redirect('nurseries-index') 

    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()  
            return redirect('nurseries-index')  
    else:
        form = PlantForm(instance=plant)

    return render(request, 'main_app/plants_form.html', {
        'form': form,
        'object': plant,  
    })


