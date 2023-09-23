from Design_patterns.parkingLot.commands.ExitCommandExecutor import ExitCommandExecutor
from Design_patterns.parkingLot.mode.mode import Mode
from Design_patterns.parkingLot.model.command import Command


class InteractiveMode(Mode):
    def __init__(self, command_executor_factory, output_printer):
        super().__init__(command_executor_factory, output_printer)

    def process(self):
        self.output_printer.welcome()
        while True:
            input_line = input()
            # input_line = ["create_parking_lot 6", "park KA-01-HH-1234 White"]

            # for ip in input_line:
            command = Command(input_line)
            self.process_command(command)
            if command.command_name == ExitCommandExecutor.COMMAND_NAME:
                break
