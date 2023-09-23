from Design_patterns.parkingLot.exception.exceptions import NumberFormatException


def is_integer(input):
    try:
        int(input)
        return True
    except NumberFormatException:
        return False
