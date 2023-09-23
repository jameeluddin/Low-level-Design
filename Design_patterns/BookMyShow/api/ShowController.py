from dataclasses import dataclass
from datetime import datetime
from typing import List

from Design_patterns.BookMyShow.services.MovieService import MovieService
from Design_patterns.BookMyShow.services.SeatAvailabilityService import SeatAvailabilityService
from Design_patterns.BookMyShow.services.ShowService import ShowService
from Design_patterns.BookMyShow.services.TheatreService import TheatreService


@dataclass
class ShowController:
    seat_availability_service: SeatAvailabilityService
    show_service: ShowService
    theatre_service: TheatreService
    movie_service: MovieService

    def create_show(self, movie_id: str, screen_id: str, start_time: datetime, duration_in_seconds: int) -> str:
        screen = self.theatre_service.get_screen(screen_id)
        movie = self.movie_service.get_movie(movie_id)
        return self.show_service.create_show(movie, screen, start_time, duration_in_seconds).id

    def get_available_seats(self, show_id: str) -> List[str]:
        show = self.show_service.get_show(show_id)
        available_seats = self.seat_availability_service.get_available_seats(show)
        return [seat.get_id() for seat in available_seats]
