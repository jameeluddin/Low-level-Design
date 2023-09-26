
class AirConditioner:
    is_on = False
    temperature = None


    def turn_on_ac(self):
        self.is_on =True
        print("AC is on")

    def turn_off_ac(self):
        self.is_on = False
        print("AC is off")

    def set_temperature(self, temp):
        self.temperature = temp
        print("Temperature changed to ", self.temperature)
