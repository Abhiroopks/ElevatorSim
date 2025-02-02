"""
File to hold data model definitions.
"""

from enum import Enum
from json import dumps
from typing import Optional


class Operation(Enum):
    PICKUP = 1
    DROPOFF = 2


class Direction(Enum):
    UP = 1
    DOWN = 2


class Request:

    def __init__(
        self,
        operation: Operation,
        floor: int,
        direction: str = "",
    ):
        self.operation = operation

        self.floor = floor

        if direction == "up":
            self.direction = Direction.UP
        elif direction == "down":
            self.direction = Direction.DOWN
        else:
            self.direction = None

    def __str__(self):
        return dumps(
            {
                "operation": self.operation.name if self.operation else None,
                "floor": self.floor,
                "direction": self.direction.name if self.direction else None,
            }
        )
