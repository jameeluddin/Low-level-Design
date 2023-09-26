from Design_patterns.FlyWeightPattern.DesignGame.IRobot import IRobot


class RoboticDog(IRobot):
    def __init__(self, type, body):
        self.type = type
        self.body = body

    def getType(self):
        return self.type

    def getBody(self):
        return self.body

    def display(self, x, y):
        pass
