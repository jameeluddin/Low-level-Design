from Design_patterns.parkingLot.commands.ColorToRegNumberCommandExecutor import ColorToRegNumberCommandExecutor
from Design_patterns.parkingLot.commands.ColorToSlotNumberCommandExecutor import ColorToSlotNumberCommandExecutor
from Design_patterns.parkingLot.commands.CreateParkingLotCommandExecutor import CreateParkingLotCommandExecutor
from Design_patterns.parkingLot.commands.ExitCommandExecutor import ExitCommandExecutor
from Design_patterns.parkingLot.commands.LeaveCommandExecutor import LeaveCommandExecutor
from Design_patterns.parkingLot.commands.ParkCommandExecutor import ParkCommandExecutor
from Design_patterns.parkingLot.commands.SlotForRegNumberCommandExecutor import SlotForRegNumberCommandExecutor
from Design_patterns.parkingLot.commands.StatusCommandExecutor import StatusCommandExecutor
from Design_patterns.parkingLot.exception.exceptions import InvalidCommandException
from Design_patterns.parkingLot.output_printer import OutputPrinter


class CommandExecutorFactory:
    def __init__(self, parking_lot_service):
        self.commands = {}
        output_printer = OutputPrinter()

        self.commands[CreateParkingLotCommandExecutor.COMMAND_NAME] = CreateParkingLotCommandExecutor(
            parking_lot_service, output_printer)
        self.commands[ParkCommandExecutor.COMMAND_NAME] = ParkCommandExecutor(
            parking_lot_service, output_printer)
        self.commands[LeaveCommandExecutor.COMMAND_NAME] = LeaveCommandExecutor(
            parking_lot_service, output_printer)
        self.commands[StatusCommandExecutor.COMMAND_NAME] = StatusCommandExecutor(
            parking_lot_service, output_printer)
        self.commands[ColorToRegNumberCommandExecutor.COMMAND_NAME] = ColorToRegNumberCommandExecutor(
            parking_lot_service, output_printer)
        self.commands[ColorToSlotNumberCommandExecutor.COMMAND_NAME] = ColorToSlotNumberCommandExecutor(
            parking_lot_service, output_printer)
        self.commands[SlotForRegNumberCommandExecutor.COMMAND_NAME] = SlotForRegNumberCommandExecutor(
            parking_lot_service, output_printer)
        self.commands[ExitCommandExecutor.COMMAND_NAME] = ExitCommandExecutor(
            parking_lot_service, output_printer)

    def get_command_executor(self, command):
        command_executor = self.commands.get(command.command_name)
        if command_executor is None:
            raise InvalidCommandException()
        return command_executor
