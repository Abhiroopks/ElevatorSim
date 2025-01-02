import logging
from core.elevator import Elevator
from cli.listener import Listener
from core.models import Request

"""
Acts as mediator between Elevator system and CLI.
"""


class Simulator:
    def __init__(self, logger: logging.Logger):
        self.logger: logging.Logger = logger
        self.quit: bool = False

    def start(self):
        elevator = Elevator(self.logger)
        listener: Listener = Listener()
        listener.start()
        requests: list = []
        while not self.quit:
            requests.clear()
            if listener.has_requests():
                request: Request = listener.pop_request()
                self.logger.info(f"Received request from cli: {request}")
                ##
                # Exit the while loop and allow process to terminate.
                if request.quit:
                    self.quit = True
                    break

                elevator.process_request(request)
