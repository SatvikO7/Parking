from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10, unique=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.slot_number


class ParkingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.SET_NULL, null=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle} - {self.entry_time}"


class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Bike', 'Bike'),
        ('Scooter', 'Scooter'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle_number} - {self.vehicle_type}"
