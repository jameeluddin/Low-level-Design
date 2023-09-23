import uuid
from Design_patterns.BookMyShow.Exceptions.NotFoundException import NotFoundException
from Design_patterns.BookMyShow.Model.Movie import Movie


class MovieService:

    def __init__(self):
        self.movies = {}

    def get_movie(self, movie_id):
        if movie_id not in self.movies:
            raise NotFoundException()
        return self.movies[movie_id]

    def create_movie(self, movie_name):
        movie_id = str(uuid.uuid4())
        movie = Movie(movie_id, movie_name)
        self.movies[movie_id] = movie
        return movie


