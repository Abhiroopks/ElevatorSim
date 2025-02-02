import logging
from core.elevator import Elevator
from cli.listener import Listener
from core.models import Request
from time import sleep

"""
Acts as mediator between Elevator system and CLI.
"""


class Simulator:
    def __init__(self, logger: logging.Logger):
        self.logger: logging.Logger = logger
        self.quit_flag: bool = False
        self.floors = 0

    def start(self) -> None:
        self.floors = int(input("Enter number of floors"))
        elevator = Elevator(self.logger, self.floors)
        listener: Listener = Listener(simulator=self)
        listener.start()
        while not self.quit_flag:
            if listener.has_requests():
                request: Request = listener.pop_request()
                self.logger.info(f"Received request from cli: {request}")

                elevator.process_request(request)

            ##
            # Let elevator take one time step to perform any actions at the moment.
            elevator.step()

            sleep(1)

    def quit(self):
        self.quit_flag = True
