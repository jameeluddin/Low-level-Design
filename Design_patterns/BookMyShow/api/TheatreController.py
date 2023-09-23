from dataclasses import dataclass

from Design_patterns.BookMyShow.services.TheatreService import TheatreService


@dataclass
class TheatreController:
    theatre_service: TheatreService

    def create_theatre(self, theatre_name: str) -> str:
        return self.theatre_service.create_theatre(theatre_name).id

    def create_screen_in_theatre(self, screen_name: str, theatre_id: str) -> str:
        theatre = self.theatre_service.get_theatre(theatre_id)
        return self.theatre_service.create_screen_in_theatre(screen_name, theatre).id

    def create_seat_in_screen(self, row_no: int, seat_no: int, screen_id: str) -> str:
        screen = self.theatre_service.get_screen(screen_id)
        return self.theatre_service.create_seat_in_screen(row_no, seat_no, screen).id
