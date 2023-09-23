from typing import List
from dataclasses import dataclass

from Design_patterns.BookMyShow.services.BookingService import BookingService
from Design_patterns.BookMyShow.services.ShowService import ShowService
from Design_patterns.BookMyShow.services.TheatreService import TheatreService


@dataclass
class BookingController:
    show_service: ShowService
    booking_service: BookingService
    theatre_service: TheatreService

    def create_booking(self, user_id: str, show_id: str, seat_ids: List[str]) -> str:
        show = self.show_service.get_show(show_id)
        seats = [self.theatre_service.get_seat(seat_id) for seat_id in seat_ids]
        return self.booking_service.create_booking(user_id, show, seats).get_id()
