from Design_patterns.parkingLot.exception.exceptions import InvalidCommandException


class Command:
    def __init__(self, input_line):
        self.SPACE = " "
        self.command_name = None
        self.params = []

        tokens_list = [token.strip() for token in input_line.strip().split(self.SPACE) if token.strip()]
        if not tokens_list:
            raise InvalidCommandException()

        self.command_name = tokens_list[0].lower()
        self.params = tokens_list[1:]
