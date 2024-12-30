from core.elevator import Elevator
from cli.listener import Listener
from time import sleep
from core.models import Request


class Simulator:
    def __init__(self, logger):
        self.logger = logger

    def start(self):
        elevator = Elevator(self.logger)
        listener = Listener()
        listener.start()
        while True:
            if listener.has_requests():
                request: Request = listener.pop_request()
                # print(request)
                ##
                # Exit the while loop and allow process to terminate.
                if request.quit:
                    break

                ##
                # Forward the request to elevator
                elevator.process_request(request=request)

            sleep(1)
