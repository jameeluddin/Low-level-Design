class OutputPrinter:
    def welcome(self):
        self.print_with_new_line("Welcome to Go-Jek Parking lot.")

    def end(self):
        self.print_with_new_line("Thanks for using Go-Jek Parking lot service.")

    def not_found(self):
        self.print_with_new_line("Not found")

    def status_header(self):
        self.print_with_new_line("Slot No.    Registration No    Colour")

    def parking_lot_full(self):
        self.print_with_new_line("Sorry, parking lot is full")

    def parking_lot_empty(self):
        self.print_with_new_line("Parking lot is empty")

    def invalid_file(self):
        self.print_with_new_line("Invalid file given.")

    def print_with_new_line(self, msg):
        print(msg)

# Example usage:
# output_printer = OutputPrinter()
# output_printer.welcome()
# output_printer.end()
# output_printer.not_found()
# output_printer.status_header()
# output_printer.parking_lot_full()
# output_printer.parking_lot_empty()
# output_printer.invalid_file()
