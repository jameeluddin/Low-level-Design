import uuid
from Design_patterns.BookMyShow.Exceptions.NotFoundException import NotFoundException
from Design_patterns.BookMyShow.Exceptions.ScreenAlreadyOccupiedException import ScreenAlreadyOccupiedException
from Design_patterns.BookMyShow.Model.Show import Show


class ShowService:

    def __init__(self):
        self.shows = {}

    def get_show(self, show_id):
        if show_id not in self.shows:
            raise NotFoundException()
        return self.shows[show_id]

    def create_show(self, movie, screen, start_time, duration_in_seconds):
        if not self.check_if_show_creation_allowed(screen, start_time, duration_in_seconds):
            raise ScreenAlreadyOccupiedException()

        show_id = str(uuid.uuid4())
        show = Show(show_id, movie, screen, start_time, duration_in_seconds)
        self.shows[show_id] = show
        return show

    def check_if_show_creation_allowed(self, screen, start_time, duration_in_seconds):
        # TODO: Implement this. This method will return whether the screen is free at a particular time for
        # specific duration. This function will be helpful in checking whether the show can be scheduled in that slot
        # or not.
        return True

