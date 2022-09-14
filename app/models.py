from django.db import models


class AmountOfSeats(models.Model):
	amount = models.IntegerField(primary_key=True, null=False)


class ProfessorSeat(models.Model):
	seat_number = models.IntegerField(primary_key=True, null=False)
	device_uuid = models.SlugField(null=True, default=None, blank=True)


class StudentSeat(models.Model):
	seat_number = models.IntegerField(primary_key=True, null=False)
	device_uuid = models.SlugField(null=False, unique=True)
