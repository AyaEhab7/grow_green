from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nurseries/', views.nurseries_index, name='nurseries-index'),
    path('nurseries/<int:nurserie_id>/', views.plant_list, name='plant-list'),
    path('store/', views.store, name='store'),
    path('store/product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('store/product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('store/product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:id>/detail/', views.product_detail, name='product-detail'),
    path('request_product/<int:product_id>/', views.product_request, name='product-request'),


]