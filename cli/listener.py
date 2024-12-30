from queue import SimpleQueue
import re
from core.models import Request, Operation
from threading import Thread

PICKUP_COMMAND_PATTERN = "^pick (\\d+) (up|down)$"
DROPOFF_COMMAND_PATTERN = "^drop (\\d+)$"


class Listener:
    def __init__(self):
        self.quit = False
        self.queue = SimpleQueue()

    def has_requests(self):
        return not self.queue.empty()

    def pop_request(self):
        return self.queue.get()

    def start(self):
        """
        Start a thread that processes stdin for requests.
        """
        thread = Thread(target=self.process_inputs)
        thread.start()

    def process_inputs(self):
        print("Listening for commands from stdin...")
        while not self.quit:
            cmd = input().strip().lower()

            if cmd == "quit":
                self.quit = True
                request = Request(quit=True)
                self.queue.put(request)
                continue

            match = None
            ##
            # Try matching pickup request
            match = re.search(pattern=PICKUP_COMMAND_PATTERN, string=cmd)
            if match:
                request = Request(
                    operation=Operation.PICKUP, floor=match[1], direction=match[2]
                )
                self.queue.put(request)
                continue

            ##
            # Try matching dropoff request
            match = re.search(pattern=DROPOFF_COMMAND_PATTERN, string=cmd)
            if match:
                request = Request(operation=Operation.DROPOFF, floor=match[1])
            if match:
                self.queue.put(request)
                continue

            print("invalid command")


if __name__ == "__main__":
    listener = Listener()
    listener.start()
