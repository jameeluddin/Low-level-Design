from Design_patterns.adapter.example2.Adaptee.WeightMachineForBabies import WeightMachineForBabies
from Design_patterns.adapter.example2.Adapter.WeightMachineAdapterImpl import WeightMachineAdapterImpl


def main():
    weight_machine_adapter = WeightMachineAdapterImpl(WeightMachineForBabies())

    print(weight_machine_adapter.get_weight_in_kg())


if __name__ == "__main__":
    main()
