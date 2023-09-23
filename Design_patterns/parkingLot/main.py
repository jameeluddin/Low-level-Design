import sys
from output_printer import OutputPrinter
from Design_patterns.parkingLot.commands.CommandExecutorFactory import CommandExecutorFactory
from Design_patterns.parkingLot.exception.exceptions import InvalidModeException
from Design_patterns.parkingLot.mode.file_mode import FileMode
from Design_patterns.parkingLot.mode.interactive_mode import InteractiveMode
from Design_patterns.parkingLot.service.ParkingLotService import ParkingLotService


def main():
    output_printer = OutputPrinter()
    parking_lot_service = ParkingLotService()
    command_executor_factory = CommandExecutorFactory(parking_lot_service)

    if is_interactive_mode():
        InteractiveMode(command_executor_factory, output_printer).process()
    elif is_file_input_mode():
        if len(sys.argv) == 2:
            file_name = sys.argv[1]
            FileMode(command_executor_factory, output_printer, file_name).process()
        else:
            raise InvalidModeException()
    else:
        raise InvalidModeException()


def is_interactive_mode():
    return len(sys.argv) == 1


def is_file_input_mode():
    return len(sys.argv) == 2


if __name__ == "__main__":
    main()
