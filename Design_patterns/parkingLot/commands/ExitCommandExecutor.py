from Design_patterns.parkingLot.commands.command_executor import CommandExecutor


class ExitCommandExecutor(CommandExecutor):
    COMMAND_NAME = "exit"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command):
        return not command.params

    def execute(self, command):
        self.output_printer.end()
