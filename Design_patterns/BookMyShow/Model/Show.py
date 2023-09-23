from dataclasses import dataclass
from datetime import datetime
from .Movie import Movie
from .Screen import Screen


@dataclass
class Show:
    id: str
    movie: Movie
    screen: Screen
    start_time: datetime
    duration_in_seconds: int
