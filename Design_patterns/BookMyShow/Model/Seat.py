from dataclasses import dataclass


@dataclass
class Seat:
    id: str
    row_no: int
    seat_no: int
