
class Screen:

    def __init__(self, id, name, theatre, seats=None):
        self.id = id
        self.name = name
        self.theatre = theatre
        self.seats = [] if seats is None else seats

    def add_seat(self, seat):
        self.seats.append(seat)
