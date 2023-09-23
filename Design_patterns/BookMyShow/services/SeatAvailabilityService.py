class SeatAvailabilityService:

    def __init__(self, booking_service, seat_lock_provider):
        self.booking_service = booking_service
        self.seat_lock_provider = seat_lock_provider

    def get_available_seats(self, show):
        all_seats = show.screen.seats
        unavailable_seats = self.get_unavailable_seats(show)

        available_seats = list(all_seats)
        available_seats = [seat for seat in all_seats if seat not in unavailable_seats]
        return available_seats

    def get_unavailable_seats(self, show):
        unavailable_seats = self.booking_service.get_booked_seats(show)
        print("llll", show)
        unavailable_seats.extend(self.seat_lock_provider.get_locked_seats(show))
        return unavailable_seats


