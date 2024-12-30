from core.states import IdleState, State
from core.models import Request


class Elevator:
    def __init__(self, logger):
        self.logger = logger
        self.state = IdleState(self, logger)

    def process_request(self, request: Request):
        self.state.process_request(request)

    def change_state(self, state: State):
        self.state = state
