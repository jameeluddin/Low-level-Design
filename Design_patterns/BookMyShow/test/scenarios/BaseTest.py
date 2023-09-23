import unittest
import random
from Design_patterns.BookMyShow.api.BookingController import BookingController
from Design_patterns.BookMyShow.api.MovieController import MovieController
from Design_patterns.BookMyShow.api.PaymentsController import PaymentsController
from Design_patterns.BookMyShow.api.ShowController import ShowController
from Design_patterns.BookMyShow.api.TheatreController import TheatreController
from Design_patterns.BookMyShow.providers.InMemorySeatLockProvider import InMemorySeatLockProvider
from Design_patterns.BookMyShow.services.BookingService import BookingService
from Design_patterns.BookMyShow.services.MovieService import MovieService
from Design_patterns.BookMyShow.services.PaymentsService import PaymentsService
from Design_patterns.BookMyShow.services.SeatAvailabilityService import SeatAvailabilityService
from Design_patterns.BookMyShow.services.ShowService import ShowService
from Design_patterns.BookMyShow.services.TheatreService import TheatreService


class BaseTest(unittest.TestCase):
    def setUp(self):
        lock_timeout = random.randint(1, 10)  # You can specify your lock timeout
        allowed_retries = random.randint(1, 5)  # You can specify the number of allowed retries
        self.setup_controllers(lock_timeout, allowed_retries)

    def setup_controllers(self, lock_timeout, allowed_retries):
        seat_lock_provider = InMemorySeatLockProvider(lock_timeout)
        booking_service = BookingService(seat_lock_provider)
        movie_service = MovieService()
        show_service = ShowService()
        theatre_service = TheatreService()
        seat_availability_service = SeatAvailabilityService(booking_service, seat_lock_provider)
        payments_service = PaymentsService(allowed_retries, seat_lock_provider)

        self.booking_controller = BookingController(show_service, booking_service, theatre_service)
        self.show_controller = ShowController(
            seat_availability_service, show_service, theatre_service, movie_service
        )
        self.theatre_controller = TheatreController(theatre_service)
        self.movie_controller = MovieController(movie_service)
        self.payments_controller = PaymentsController(payments_service, booking_service)

    def validate_seats_list(self, seats_list, all_seats_in_screen, excluded_seats):
        for included_seat in all_seats_in_screen:
            if included_seat not in excluded_seats:
                self.assertTrue(included_seat in seats_list)

        for excluded_seat in excluded_seats:
            self.assertFalse(excluded_seat in seats_list)

    def create_seats(self, theatre_controller, screen, num_rows, num_seats_in_row):
        seats = []
        for row in range(num_rows):
            for seat_no in range(num_seats_in_row):
                seat = theatre_controller.create_seat_in_screen(row, seat_no, screen)
                seats.append(seat)
        return seats

    def setup_screen(self):
        theatre = self.theatre_controller.create_theatre("Theatre 1")
        return self.theatre_controller.create_screen_in_theatre("Screen 1", theatre)


if __name__ == "__main__":
    unittest.main()
