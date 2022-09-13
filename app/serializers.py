from rest_framework import serializers
from app import models


class SeatSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Seat
		fields = ['seat_number', 'device_uuid']
