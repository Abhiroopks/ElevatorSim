from typing import List
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
        self.floor: int = 0
        self.top_floor: int = floors
        self.bottom_floor: int = 0
        self.dropoffs: List[bool] = [False] * self.top_floor
        self.pickups: List[bool] = [False] * self.top_floor

    def process_request(self, request: Request) -> None:
        self.state.process_request(request)

    def change_state(self, state: "State") -> None:
        self.state = state

    def step(self) -> None:
        self.state.step()

    def has_dropoff(self) -> bool:
        return self.dropoffs[self.floor]

    def has_pickup(self) -> bool:
        return self.pickups[self.floor]

    def remove_pickup(self) -> None:
        self.pickups[self.floor] = False

    def remove_dropoff(self) -> None:
        self.dropoffs[self.floor] = False

    def add_pickup(self, floor: int) -> None:
        self.pickups[floor] = True

    def add_dropoff(self, floor: int) -> None:
        self.dropoffs[floor] = True

    def move_up(self) -> None:
        self.logger.info(f"Moving up from floor {self.floor} to {self.floor+1}")
        self.floor += 1

    def move_down(self) -> None:
        self.logger.info(f"Moving down from floor {self.floor} to {self.floor-1}")
        self.floor -= 1

    def has_requests_above(self) -> bool:
        for i in range(self.floor, self.top_floor):
            if self.dropoffs[i] or self.pickups[i]:
                return True
        return False

    def has_requests_below(self) -> bool:
        for i in range(self.bottom_floor, self.floor):
            if self.dropoffs[i] or self.pickups[i]:
                return True
        return False


class State(ABC):
    """
    Abstract class for elevator States
    """

    def __init__(self, elevator: Elevator, logger: logging.Logger):  # type: ignore
        super().__init__()

        self.elevator: "Elevator" = elevator  # type: ignore
        self.logger: logging.Logger = logger

    def process_request(self, request: Request):
        if request.operation == Operation.PICKUP:
            self.elevator.add_pickup(request.floor)
        if request.operation == Operation.DROPOFF:
            self.elevator.add_dropoff(request.floor)

    @abstractmethod
    def step(self):
        pass


class IdleState(State):

    def step(self):
        if self.elevator.has_requests_above():
            self.elevator.change_state(MovingUpState(self.elevator, self.logger))
        elif self.elevator.has_requests_below():
            self.elevator.change_state(MovingDownState(self.elevator, self.logger))


class MovingUpState(State):

    def step(self):
        if self.elevator.has_dropoff() or self.elevator.has_pickup():
            self.elevator.change_state(OpeningDoorState(self.elevator, self.logger))
            self.elevator.remove_dropoff()
            self.elevator.remove_pickup()
        else:
            self.elevator.move_up()


class MovingDownState(State):

    def step(self):
        if self.elevator.has_dropoff() or self.elevator.has_pickup():
            self.elevator.change_state(OpeningDoorState(self.elevator, self.logger))
            self.elevator.remove_dropoff()
            self.elevator.remove_pickup()
        else:
            self.elevator.move_down()


class OpeningDoorState(State):

    def step(self):
        self.logger.info(f"Opening door at floor {self.elevator.floor}")
        self.elevator.change_state(LoadingState(self.elevator, self.logger))


class ClosingDoorState(State):

    def step(self):
        self.logger.info(f"Closing door at floor {self.elevator.floor}")
        if self.elevator.has_requests_above():
            self.elevator.change_state(MovingUpState(self.elevator, self.logger))
        elif self.elevator.has_requests_below():
            self.elevator.change_state(MovingDownState(self.elevator, self.logger))
        else:
            self.elevator.change_state(IdleState(self.elevator, self.logger))


class LoadingState(State):

    def step(self):
        self.logger.info(
            f"Loading / Dropping passengers at floor {self.elevator.floor}"
        )
        self.elevator.change_state(ClosingDoorState(self.elevator, self.logger))
