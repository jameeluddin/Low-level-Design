from Design_patterns.HandleNullObject.vehicle import Vehicle


class NullVehicle(Vehicle):

    def getTankCapacity(self):
        return 0

    def getSeatingCapacity(self):
        return 0
