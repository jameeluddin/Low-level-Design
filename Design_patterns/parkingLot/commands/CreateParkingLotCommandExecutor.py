from Design_patterns.parkingLot.commands.command_executor import CommandExecutor
from Design_patterns.parkingLot.model.parking_lot import ParkingLot
from Design_patterns.parkingLot.model.parking_strategy.Natural_ordering_parking_strategy import NaturalOrderingParkingStrategy


class CreateParkingLotCommandExecutor(CommandExecutor):
    COMMAND_NAME = "create_parking_lot"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command):
        params = command.params
        if len(params) != 1:
            return False
        return params[0].isdigit()

    def execute(self, command):
        parking_lot_capacity = int(command.params[0])
        parking_lot = ParkingLot(parking_lot_capacity)
        self.parking_lot_service.create_parking_lot(parking_lot, NaturalOrderingParkingStrategy())
        self.output_printer.print_with_new_line(
            f"Created a parking lot with {parking_lot.get_capacity()} slots")
