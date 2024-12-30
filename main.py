from core.simulator import Simulator
import logging


def main():
    ##
    # Setup logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="elevator.log", level=logging.INFO)

    ##
    # Start the simulator
    sim = Simulator(logger)
    sim.start()


if __name__ == "__main__":
    main()
