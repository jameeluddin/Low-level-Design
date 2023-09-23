import unittest
import datetime

from Design_patterns.BookMyShow.test.scenarios.BaseTest import BaseTest


class Case2Tests(BaseTest):

    def setUp(self):
        self.setup_controllers(10, 0)

    def test_case_2(self):
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

        u2_available_seats = self.show_controller.get_available_seats(show)

        # Validate that u2 seats has all screen seats except the ones already blocked by u1
        self.validate_seats_list(u2_available_seats, screen1_seat_ids, u1_selected_seats)

        self.payments_controller.payment_failed(booking_id, user1)

        u2_available_seats_after_payment_failure = self.show_controller.get_available_seats(show)
        # Since u1's payment has failed so u2 should now get back all the seats.
        self.validate_seats_list(u2_available_seats_after_payment_failure, screen1_seat_ids, [])


if __name__ == '__main__':
    unittest.main()
