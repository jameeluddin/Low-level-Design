
from abc import ABC, abstractmethod


class RateLimiter(ABC):

    @abstractmethod
    def grant_access(self):
        pass
