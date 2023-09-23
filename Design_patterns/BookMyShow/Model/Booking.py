from enum import Enum
from dataclasses import dataclass
from typing import List

from .Show import Show
from .Seat import Seat
from .BookingStatus import BookingStatus
from ..Exceptions.InvalidStateException import InvalidStateException


@dataclass
class Booking:
    id: str
    show: Show
    seats_booked: List[Seat]
    user: str
    booking_status: BookingStatus = BookingStatus.Created

    def is_confirmed(self):
        return self.booking_status == BookingStatus.Confirmed

    def confirm_booking(self):
        if self.booking_status != BookingStatus.Created:
            raise InvalidStateException()

        self.booking_status = BookingStatus.Confirmed

    def expire_booking(self):
        if self.booking_status != BookingStatus.Created:
            raise InvalidStateException()

        self.booking_status = BookingStatus.Expired
