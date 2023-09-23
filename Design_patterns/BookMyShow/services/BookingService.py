from collections import defaultdict
from typing import List
import uuid
from Design_patterns.BookMyShow.Exceptions.BadRequestException import BadRequestException
from Design_patterns.BookMyShow.Exceptions.NotFoundException import NotFoundException
from Design_patterns.BookMyShow.Exceptions.SeatPermanentlyUnavailableException import SeatPermanentlyUnavailableException
from Design_patterns.BookMyShow.Model.Booking import Booking


class BookingService:

    def __init__(self, seat_lock_provider):
        self.seat_lock_provider = seat_lock_provider
        self.show_bookings = {}

    def get_booking(self, booking_id):
        if booking_id not in self.show_bookings:
            raise NotFoundException()
        return self.show_bookings[booking_id]

    def get_all_bookings(self, show):
        response = []
        for booking in self.show_bookings.values():
            if booking.show == show:
                response.append(booking)
        return response

    def create_booking(self, user_id, show, seats):
        if self.is_any_seat_already_booked(show, seats):
            raise SeatPermanentlyUnavailableException()

        self.seat_lock_provider.lock_seats(show, seats, user_id)
        booking_id = str(uuid.uuid4())
        new_booking = Booking(booking_id, show, user_id, seats)
        self.show_bookings[booking_id] = new_booking
        return new_booking
        # TODO: Create timer for booking expiry

    def get_booked_seats(self, show):
        return [seat for booking in self.get_all_bookings(show) if booking.is_confirmed()
                for seat in booking.seats_booked]

    def confirm_booking(self, booking, user):
        if booking.user != user:
            raise BadRequestException()

        for seat in booking.seats_booked:
            if not self.seat_lock_provider.validate_lock(booking.show, seat, user):
                raise BadRequestException()
        booking.confirm_booking()

    def is_any_seat_already_booked(self, show, seats):
        booked_seats = self.get_booked_seats(show)
        return any(seat in booked_seats for seat in seats)



