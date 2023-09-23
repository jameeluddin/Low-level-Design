from Design_patterns.factoryPattern.circle import Circle
from Design_patterns.factoryPattern.rectangle import Rectangle


def get_shape(argument):
    switcher = {
        "CIRCLE": Circle(),
        "RECTANGLE": Rectangle()
    }

    return switcher.get(argument, None)
