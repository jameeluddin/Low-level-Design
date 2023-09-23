from Design_patterns.parkingLot.commands.command_executor import CommandExecutor


class SlotForRegNumberCommandExecutor(CommandExecutor):
    COMMAND_NAME = "slot_number_for_registration_number"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command):
        params = command.params
        return len(params) == 1

    def execute(self, command):
        occupied_slots = self.parking_lot_service.get_occupied_slots()
        reg_number_to_find = command.params[0]
        found_slot = next(
            (slot for slot in occupied_slots if slot.parked_car.registration_number == reg_number_to_find),
            None
        )
        if found_slot:
            self.output_printer.print_with_new_line(str(found_slot.slot_number))
        else:
            self.output_printer.not_found()
