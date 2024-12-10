from django.urls import path
from . import views 

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('nurseries/', views.nurseries_index, name='nurseries-index'),
    path('nurseries/<int:nurserie_id>/', views.plant_list, name='plant-list'),
    path('plants/<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('plants/create/', views.add_plant, name='add_plant'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),
    path('plants/<int:plant_id>/add/', views.add_nursery_care, name='add_nursery_care'),
    path('plants/<int:plant_id>/add_status/', views.add_status, name='add_status'),
    path('store/', views.store, name='store'),
    path('store/product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('store/product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('store/product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:id>/detail/', views.product_detail, name='product-detail'),
   
  #request 
    path('store/product/request/<int:product_id>/', views.product_request, name='product-request'),
    path('store/product/request/<int:product_request_id>/detail/', views.product_request_detail, name='product-request-detail'),
    path('store/product/request/<int:product_request_id>/edit/', views.ProductRequestUpdateView.as_view(), name='product-request-edit'),
    path('store/product/request/<int:product_request_id>/delete/', views.ProductRequestDeleteView.as_view(), name='product-request-delete'),

]

