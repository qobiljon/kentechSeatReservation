from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import status
from random import randint

from app.serializers import SeatSerializer
from app.models import StudentSeat
from app.models import ProfessorSeat
from app.services import get_amount_of_seats


@require_http_methods(['GET'])
def redirect_to_student(request):
	return redirect(to='student')


@require_http_methods(['GET'])
def index(request):
	return render(
		request=request,
		template_name='index.html',
		context={
			'is_professor': 'professor' in request.path,
			'is_student': 'student' in request.path,
		}
	)


@require_http_methods(['GET'])
def get_professor_seat(request):
	if 'device_uuid' not in request.GET:
		return JsonResponse({'msg': 'device_uuid paramter must be presented'}, status=status.HTTP_400_BAD_REQUEST)

	device_uuid = request.GET['device_uuid']
	if ProfessorSeat.objects.filter(device_uuid=device_uuid).exists():
		seat = ProfessorSeat.objects.get(device_uuid=device_uuid)
	else:
		all_numbers = list(map(lambda x: x.seat_number, ProfessorSeat.objects.filter(device_uuid=None)))
		if len(all_numbers) == 0:
			return JsonResponse({'msg': 'no more professor seats left'}, status=status.HTTP_400_BAD_REQUEST)
		selected_seat_numnber = all_numbers[randint(0, len(all_numbers) - 1)]
		seat = ProfessorSeat.objects.get(seat_number=selected_seat_numnber)
		seat.device_uuid = device_uuid
		seat.save()

	serializer = SeatSerializer(seat)
	return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)


@require_http_methods(['GET'])
def get_student_seat(request):
	if 'device_uuid' not in request.GET:
		return JsonResponse({'msg': 'device_uuid paramter must be presented'}, status=status.HTTP_400_BAD_REQUEST)

	device_uuid = request.GET['device_uuid']
	if StudentSeat.objects.filter(device_uuid=device_uuid).exists():
		seat = StudentSeat.objects.get(device_uuid=device_uuid)
	else:
		available_numbers = set(range(1, get_amount_of_seats().amount + 1))
		professor_seat_numbers = list(map(lambda x: x.seat_number, ProfessorSeat.objects.all()))
		reserved_seat_numbers = set(professor_seat_numbers + list(map(lambda x: x.seat_number, StudentSeat.objects.all())))

		for seat_number in reserved_seat_numbers: available_numbers.remove(seat_number)
		available_numbers = list(available_numbers)

		seat_numer = available_numbers[randint(0, len(available_numbers) - 1)]
		seat = StudentSeat.objects.create(device_uuid=device_uuid, seat_number=seat_numer)

	serializer = SeatSerializer(seat)
	return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
