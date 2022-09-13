from django.db import models


class Seat(models.Model):
	seat_number = models.IntegerField(primary_key=True, null=False)
	device_uuid = models.SlugField(null=False, unique=True)
