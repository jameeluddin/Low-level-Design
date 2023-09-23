from Design_patterns.parkingLot.commands.command_executor import CommandExecutor


class LeaveCommandExecutor(CommandExecutor):
    COMMAND_NAME = "leave"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command):
        params = command.params
        if len(params) != 1:
            return False
        return params[0].isdigit()

    def execute(self, command):
        slot_num = int(command.params[0])
        self.parking_lot_service.make_slot_free(slot_num)
        self.output_printer.print_with_new_line(f"Slot number {slot_num} is free")
