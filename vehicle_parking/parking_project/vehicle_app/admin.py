from django.contrib import admin
from .models import Vehicle
from .models import ParkingSlot, ParkingHistory

admin.site.register(ParkingSlot)
admin.site.register(ParkingHistory)


admin.site.register(Vehicle)
