import uuid

from Design_patterns.BookMyShow.Exceptions.NotFoundException import NotFoundException
from Design_patterns.BookMyShow.Model.Screen import Screen
from Design_patterns.BookMyShow.Model.Seat import Seat
from Design_patterns.BookMyShow.Model.Theatre import Theatre


class TheatreService:

    def __init__(self):
        self.theatres = {}
        self.screens = {}
        self.seats = {}

    def get_seat(self, seat_id):
        if seat_id not in self.seats:
            raise NotFoundException()
        return self.seats[seat_id]

    def get_theatre(self, theatre_id):
        if theatre_id not in self.theatres:
            raise NotFoundException()
        return self.theatres[theatre_id]

    def get_screen(self, screen_id):
        if screen_id not in self.screens:
            raise NotFoundException()
        return self.screens[screen_id]

    def create_theatre(self, theatre_name):
        theatre_id = str(uuid.uuid4())
        theatre = Theatre(theatre_id, theatre_name)
        self.theatres[theatre_id] = theatre
        return theatre

    def create_screen_in_theatre(self, screen_name, theatre):
        screen = self.create_screen(screen_name, theatre)
        theatre.add_screen(screen)
        return screen

    def create_seat_in_screen(self, row_no, seat_no, screen):
        seat_id = str(uuid.uuid4())
        seat = Seat(seat_id, row_no, seat_no)
        self.seats[seat_id] = seat
        screen.add_seat(seat)
        return seat

    def create_screen(self, screen_name, theatre):
        screen_id = str(uuid.uuid4())
        screen = Screen(screen_id, screen_name, theatre)
        self.screens[screen_id] = screen
        return screen

