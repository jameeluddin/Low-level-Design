from Design_patterns.BookMyShow.Exceptions.BadRequestException import BadRequestException


class PaymentsService:

    def __init__(self, allowed_retries, seat_lock_provider):
        self.booking_failures = {}
        self.allowed_retries = allowed_retries
        self.seat_lock_provider = seat_lock_provider

    def process_payment_failed(self, booking, user):
        if booking.user != user:
            raise BadRequestException()

        if booking not in self.booking_failures:
            self.booking_failures[booking] = 0

        current_failures_count = self.booking_failures[booking]
        new_failures_count = current_failures_count + 1
        self.booking_failures[booking] = new_failures_count

        if new_failures_count > self.allowed_retries:
            self.seat_lock_provider.unlock_seats(booking.show, booking.seats_booked, booking.user)

