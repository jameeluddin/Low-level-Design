from Design_patterns.parkingLot.commands.command_executor import CommandExecutor


class StatusCommandExecutor(CommandExecutor):
    COMMAND_NAME = "status"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command):
        return not command.params

    def execute(self, command):
        occupied_slots = self.parking_lot_service.get_occupied_slots()

        if not occupied_slots:
            self.output_printer.parking_lot_empty()
            return

        self.output_printer.status_header()
        for slot in occupied_slots:
            parked_car = slot.parked_car
            slot_number = str(slot.slot_number)

            self.output_printer.print_with_new_line(
                self.pad_string(slot_number, 12) + self.pad_string(parked_car.registration_number, 19) + parked_car.color
            )

    @staticmethod
    def pad_string(word, length):
        new_word = word
        while len(new_word) < length:
            new_word += " "
        return new_word
