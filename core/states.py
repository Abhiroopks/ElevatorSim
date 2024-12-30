from abc import ABC, abstractmethod
from core.models import Request


class State(ABC):
    """
    Abstract class for elevator States
    """

    def __init__(self, context, logger):
        self.context = context
        self.logger = logger
        super().__init__()

    @abstractmethod
    def process_request(self, request: Request):
        pass


class IdleState(State):

    def process_request(self, request: Request):
        print(request)


class MovingUpState(State):

    def process_request(self, request: Request):
        print(request)


class MovingDownState(State):

    def process_request(self, request: Request):
        print(request)
