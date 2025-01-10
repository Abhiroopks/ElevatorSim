from core.states import IdleState, State
from core.models import Request


class Elevator:
    def __init__(self, logger):
        self.logger = logger
        ##
        # Initializes to Idle State.
        self.state: State = IdleState(self, logger)
        self.floor: int = 1

    def process_request(self, request: Request):
        self.state.process_request(request)

    def change_state(self, state: State):
        self.state = state
