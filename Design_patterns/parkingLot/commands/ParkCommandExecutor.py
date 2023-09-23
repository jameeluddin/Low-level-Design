from Design_patterns.parkingLot.commands.command_executor import CommandExecutor
from Design_patterns.parkingLot.exception.exceptions import NoFreeSlotAvailableException
from Design_patterns.parkingLot.model.car import Car


class ParkCommandExecutor(CommandExecutor):
    COMMAND_NAME = "park"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command):
        params = command.params
        return len(params) == 2

    def execute(self, command):
        car = Car(command.params[0], command.params[1])
        try:
            slot = self.parking_lot_service.park(car)
            self.output_printer.print_with_new_line(f"Allocated slot number: {slot}")
        except NoFreeSlotAvailableException as exception:
            self.output_printer.parking_lot_full()
