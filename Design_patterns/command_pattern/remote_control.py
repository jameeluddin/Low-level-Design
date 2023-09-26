
class RemoteControl:
    def __init__(self, command=None):
        self.ac_command_history = list()
        self.command = command

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.ac_command_history.append(self.command)

    def undo(self):
        if len(self.ac_command_history) > 0:
            last_command = self.ac_command_history[-1]
            last_command.undo()

