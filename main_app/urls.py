from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nurseries/', views.nurseries_index, name='nurseries-index'),
    path('nurseries/<int:nurserie_id>/', views.plant_list, name='plant-list'),
    path('store/', views.store, name='store'),
    path('request_product/<int:product_id>/', views.product_request, name='product-request'),
]