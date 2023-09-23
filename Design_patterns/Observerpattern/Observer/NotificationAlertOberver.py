from abc import ABC, abstractmethod


class NotificationObserver(ABC):

    @abstractmethod
    def update(self):
        pass
