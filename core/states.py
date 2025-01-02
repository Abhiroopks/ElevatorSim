from abc import ABC, abstractmethod
import logging
from core.models import Request, Operation


class State(ABC):
    """
    Abstract class for elevator States
    """

    def __init__(self, context: "Elevator", logger: logging.Logger):  # type: ignore
        self.elevator: "Elevator" = context  # type: ignore
        self.logger: logging.Logger = logger
        super().__init__()

    @abstractmethod
    def process_request(self, request: Request):
        pass


class IdleState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass


class MovingUpState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass


class MovingDownState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass
