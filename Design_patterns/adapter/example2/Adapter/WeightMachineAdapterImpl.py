from Design_patterns.adapter.example2.Adapter.WeightMachineAdapter import WeightMachineAdapter


class WeightMachineAdapterImpl(WeightMachineAdapter):
    def __init__(self, weight_machine):
        self.weight_machine = weight_machine

    def get_weight_in_kg(self):
        weight_in_pound = self.weight_machine.get_weight_in_pound()
        weight_in_kg = weight_in_pound * 0.45
        return weight_in_kg
