from Design_patterns.parkingLot.mode.mode import Mode


class FileMode(Mode):
    def __init__(self, command_executor_factory, output_printer, file_name):
        super().__init__(command_executor_factory, output_printer)
        self.file_name = file_name

    def process(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    command = Command(line.strip())
                    self.process_command(command)
        except FileNotFoundError:
            self.output_printer.invalid_file()
