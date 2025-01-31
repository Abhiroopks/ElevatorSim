from core.simulator import Simulator
import logging


def main() -> None:
    ##
    # Setup logging
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(filename="elevator.log", level=logging.INFO)

    ##
    # Start the simulator
    sim: Simulator = Simulator(logger)
    sim.start()


if __name__ == "__main__":
    main()
