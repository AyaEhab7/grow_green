from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nurseries/', views.nurseries_index, name='nurseries-index'),
    path('nurseries/<int:nurserie_id>/', views.plant_list, name='plant-list'),
    path('plants/<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),
    path('plants/<int:plant_id>/add/', views.add_nursery_care, name='add_nursery_care'),
]