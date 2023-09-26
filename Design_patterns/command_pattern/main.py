from Design_patterns.command_pattern.AirConditioner import AirConditioner
from Design_patterns.command_pattern.TurnACOffCommand import TurnAcOffCommand
from Design_patterns.command_pattern.TurnAcOnCommand import TurnAcOnCommand
from Design_patterns.command_pattern.remote_control import RemoteControl


def main():
    air_conditioner = AirConditioner()
    remote_obj = RemoteControl()
    remote_obj.set_command(TurnAcOffCommand(air_conditioner))
    # remote_obj.set_command(TurnAcOnCommand(air_conditioner))
    remote_obj.press_button()
    remote_obj.undo()



if __name__ == '__main__':
    main()