from Design_patterns.command_pattern.command import ICommand


class TurnAcOffCommand(ICommand):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.turn_off_ac()

    def undo(self):
        self.ac.turn_on_ac()
