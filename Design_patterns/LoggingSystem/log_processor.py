from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def log(self, request, msg):
        pass


class LogProcessor(Handler):
    _next_handler = None
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def log(self, request, msg):
        if self._next_handler:
            return self._next_handler.log(request, msg)

        return None
