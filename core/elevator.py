from core.models import Request
from abc import ABC, abstractmethod
import logging
from core.models import Request, Operation


class Elevator:
    def __init__(self, logger, floors: int):
        self.logger = logger
        ##
        # Initializes to Idle State.
        self.state: State = IdleState(self, logger)
        self.floor: int = 1
        self.top_floor: int = floors
        self.bottom_floor: int = 0

    def process_request(self, request: Request) -> None:
        self.state.process_request(request)

    def change_state(self, state: "State") -> None:
        self.state = state

    def step(self) -> None:
        self.state.step()


class State(ABC):
    """
    Abstract class for elevator States
    """

    def __init__(self, elevator: Elevator, logger: logging.Logger):  # type: ignore
        super().__init__()

        self.elevator: "Elevator" = elevator  # type: ignore
        self.logger: logging.Logger = logger

    @abstractmethod
    def process_request(self, request: Request):
        pass

    @abstractmethod
    def step(self):
        pass


class IdleState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass

    def step(self):
        self.logger.info("Elevator is idle, nothing to do this step.")


class MovingUpState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass

    def step(self):
        pass


class MovingDownState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass

    def step(self):
        pass


class OpeningDoorState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass

    def step(self):
        pass


class ClosingDoorState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass

    def step(self):
        pass


class LoadingState(State):

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            pass
        if request.operation == Operation.DROPOFF:
            pass

    def step(self):
        pass
