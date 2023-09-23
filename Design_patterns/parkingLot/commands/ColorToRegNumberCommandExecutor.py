from Design_patterns.parkingLot.commands.command_executor import CommandExecutor


class ColorToRegNumberCommandExecutor(CommandExecutor):
    COMMAND_NAME = "registration_numbers_for_cars_with_colour"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command):
        return len(command.params) == 1

    def execute(self, command):
        color = command.params[0]
        slots_for_color = self.parking_lot_service.get_slots_for_color(color)
        if not slots_for_color:
            self.output_printer.not_found()
        else:
            registration_numbers = [slot.parked_car.registration_number for slot in slots_for_color]
            result = ", ".join(registration_numbers)
            self.output_printer.print_with_new_line(result)
