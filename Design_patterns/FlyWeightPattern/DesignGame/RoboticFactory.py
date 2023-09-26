from Design_patterns.FlyWeightPattern.DesignGame.HumanoidRobot import HumanoidRobot
from Design_patterns.FlyWeightPattern.DesignGame.RoboticDog import RoboticDog

char_cache = dict()


class Sprites:
    pass


class RoboticFactory:
    global char_cache

    def createRobot(self, robot_type):
        if char_cache.get(robot_type):
            return char_cache.get(robot_type)
        else:
            if robot_type == "HUMANOID":
                humanoid_sprite = Sprites()
                humanoid_object = HumanoidRobot(robot_type, humanoid_sprite)
                char_cache[robot_type] = humanoid_object
                return humanoid_object
            else:
                robotic_dog_sprite = Sprites()
                robotic_dog_object = RoboticDog(robot_type, robotic_dog_sprite)
                char_cache[robot_type] = robotic_dog_object
                return robotic_dog_object
