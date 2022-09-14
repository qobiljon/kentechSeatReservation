from app.models import AmountOfSeats


def get_amount_of_seats() -> AmountOfSeats:
	if AmountOfSeats.objects.count() == 0:
		AmountOfSeats.objects.create(amount=140)
	return AmountOfSeats.objects.first()
