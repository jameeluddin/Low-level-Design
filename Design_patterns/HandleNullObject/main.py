from Design_patterns.HandleNullObject.VehicleFactory import VehicleFactory


def print_vehicle_details(vehicle):
    print("Seating Capacity", vehicle.getSeatingCapacity())
    print("Fuel Tank Capacity", vehicle.getTankCapacity())


def main():
    vehicle = VehicleFactory().getVehicleObject("Car")
    print_vehicle_details(vehicle)


if __name__ == "__main__":
    main()
