from django.urls import path

from . import views

urlpatterns = [
    path('vehicles/register/', views.register_vehicle, name='register_vehicle'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/edit/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicles/delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('history/', views.parking_history, name='parking_history'),
    path('admin/history/', views.admin_parking_history_view, name='admin_parking_history'),
    path('accounts/register/', views.register_view, name='register'),  # User signup/register
    
]


