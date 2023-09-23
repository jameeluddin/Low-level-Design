import unittest
import datetime

from BaseTest import BaseTest


class Case1Tests(BaseTest):
    def setUp(self):
        self.setup_controllers(10, 0)

    def test_case1(self):
        user1 = "User1"
        user2 = "User2"

        movie = self.movie_controller.create_movie("Movie 1")
        screen = self.setup_screen()
        screen1_seat_ids = self.create_seats(self.theatre_controller, screen, 2, 10)

        show = self.show_controller.create_show(movie, screen, datetime.datetime.now(), 2 * 60 * 60)

        u1_available_seats = self.show_controller.get_available_seats(show)

        # Validate that seats u1 received has all screen seats
        self.validate_seats_list(u1_available_seats, screen1_seat_ids, [])

        u1_selected_seats = [
            screen1_seat_ids[0],
            screen1_seat_ids[2],
            screen1_seat_ids[5],
            screen1_seat_ids[10]
        ]
        booking_id = self.booking_controller.create_booking(user1, show, u1_selected_seats)
        self.payments_controller.payment_success(booking_id, user1)

        u2_available_seats = self.show_controller.get_available_seats(show)
        # Validate that u2 seats has all screen seats except the ones already booked by u1
        self.validate_seats_list(u2_available_seats, screen1_seat_ids, u1_selected_seats)


if __name__ == "__main__":
    unittest.main()
