from Design_patterns.adapter.example2.Adaptee.WeightMachine import WeightMachine


class WeightMachineForBabies(WeightMachine):

    def get_weight_in_pound(self):
        return 28

