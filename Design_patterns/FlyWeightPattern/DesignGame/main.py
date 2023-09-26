from Design_patterns.FlyWeightPattern.DesignGame.RoboticFactory import RoboticFactory


def main():
    humanoid_robot_1 = RoboticFactory().createRobot("HUMANOID")
    humanoid_robot_1.display(1, 2)

    humanoid_robot_2 = RoboticFactory().createRobot("HUMANOID")
    humanoid_robot_2.display(10, 30)

    robo_dog_1 = RoboticFactory().createRobot("ROBOTICDOG")
    robo_dog_1.display(2, 9)

    robo_dog_2 = RoboticFactory().createRobot("ROBOTICDOG")
    robo_dog_2.display(11, 19)




if __name__ == "__main__":
    main()
