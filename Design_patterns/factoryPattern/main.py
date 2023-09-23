from Design_patterns.factoryPattern.shapeFactory import get_shape


def main():
    shapeFactoryObj = get_shape("CIRCLE")
    shapeFactoryObj.draw()


if __name__ == "__main__":
    main()