from dataclasses import dataclass

from Design_patterns.BookMyShow.services.MovieService import MovieService


@dataclass
class MovieController:
    movie_service: MovieService

    def create_movie(self, movie_name: str) -> str:
        return self.movie_service.create_movie(movie_name).id
