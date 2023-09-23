from Design_patterns.HandleNullObject.NUllVehicle import NullVehicle
from Design_patterns.HandleNullObject.car import Car


class VehicleFactory:
    def getVehicleObject(self, type_of_vehicle):

        if type_of_vehicle == "Car":
            return Car()

        return NullVehicle()