
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from vehicle_app import views as vehicle_views
from vehicle_app import views




urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='vehicle_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('vehicles/', include('vehicle_app.urls')),  # All vehicle-related URLs here
    path('', vehicle_views.home, name='home'),

    path('parking/history/', vehicle_views.admin_parking_history_view, name='admin_parking_history'),



]
