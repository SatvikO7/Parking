from django.shortcuts import render, redirect
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import get_object_or_404
from .forms import VehicleForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import ParkingSlot, ParkingHistory
from django.contrib.auth.decorators import login_required
from .models import ParkingHistory

from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, redirect
from .forms import StudentRegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or auto-login + redirect to dashboard
    else:
        form = UserCreationForm()
    return render(request, 'vehicle_app/register.html', {'form': form})




@staff_member_required
def admin_parking_history_view(request):
    history = ParkingHistory.objects.select_related('user', 'vehicle', 'slot').order_by('-entry_time')
    return render(request, 'vehicle_app/admin_parking_history.html', {'history': history})


@login_required
def parking_history_view(request):
    history = ParkingHistory.objects.filter(user=request.user).select_related('vehicle', 'slot').order_by('-parked_at')
    return render(request, 'vehicle_app/parking_history.html', {'history': history})


@login_required
def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user

            # Find an available parking slot
            available_slot = ParkingSlot.objects.filter(is_occupied=False).first()
            print(f"Available slot found: {available_slot}")

            if available_slot:
                available_slot.is_occupied = True
                available_slot.save()

                # Save the vehicle with assigned user
                vehicle.save()
                print(f"Vehicle saved: {vehicle}")

                # Create parking history record here
                ParkingHistory.objects.create(
                    user=request.user,
                    vehicle=vehicle,
                    slot=available_slot
                )
                print("ParkingHistory record created")

                return redirect('vehicle_list')  # Redirect after successful registration
            else:
                form.add_error(None, "No parking slots available.")
                print("No parking slots available.")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = VehicleForm()
    return render(request, 'vehicle_app/register_vehicle.html', {'form': form})



def home(request):
    return render(request, 'vehicle_app/home.html')

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'vehicle_app/vehicle_list.html', {'vehicles': vehicles})


@login_required
def parking_history(request):
    history = ParkingHistory.objects.filter(user=request.user).order_by('-entry_time')
    return render(request, 'vehicle_app/parking_history.html', {'history': history})


@login_required
def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_app/register_vehicle.html', {'form': form})

@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    vehicle.delete()
    return redirect('vehicle_list')


@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(user=request.user)

    # Get the search query from the GET request
    search_query = request.GET.get('search', '')
    if search_query:
        vehicles = vehicles.filter(model__icontains=search_query)

    return render(request, 'vehicle_app/vehicle_list.html', {'vehicles': vehicles})


@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, 'vehicle_app/vehicle_list.html', {'vehicles': vehicles})





