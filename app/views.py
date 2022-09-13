from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from random import randint

from app.serializers import SeatSerializer
from app.models import Seat


@require_http_methods(['GET'])
def index(request):
	return render(request, 'index.html')


@require_http_methods(['GET'])
def get_seat(request):
	if 'device_uuid' not in request.GET:
		return JsonResponse({'msg': 'device_uuid paramter must be presented'}, status=status.HTTP_400_BAD_REQUEST)

	device_uuid = request.GET['device_uuid']
	if Seat.objects.filter(device_uuid=device_uuid).exists():
		seat = Seat.objects.get(device_uuid=device_uuid)
	else:
		all_numbers = set(range(1, 141))
		for seat in Seat.objects.all():
			all_numbers.remove(seat.seat_number)
		all_numbers = list(all_numbers)

		seat_numer = all_numbers[randint(0, len(all_numbers) - 1)]
		seat = Seat.objects.create(device_uuid=device_uuid, seat_number=seat_numer)

	serializer = SeatSerializer(seat)
	return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
