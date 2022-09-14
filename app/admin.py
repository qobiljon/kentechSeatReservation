from django.contrib import admin

from app.models import AmountOfSeats
from app.models import ProfessorSeat
from app.models import StudentSeat


@admin.register(AmountOfSeats)
class AmountOfSeatsAdmin(admin.ModelAdmin):
	list_display = ('amount',)


@admin.register(StudentSeat)
class StudentSeatAdmin(admin.ModelAdmin):
	list_display = ('seat_number', 'device_uuid')


@admin.register(ProfessorSeat)
class ProfessorSeatAdmin(admin.ModelAdmin):
	list_display = ('seat_number', 'device_uuid')
