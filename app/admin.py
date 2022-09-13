from django.contrib import admin

from app.models import Seat


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
	list_display = ('seat_number', 'device_uuid')
