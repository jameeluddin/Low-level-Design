from Design_patterns.FlyWeightPattern.wordProcessor.LetterFactor import LetterFactor


def main():
    obj1 = LetterFactor().create_letter('t')
    obj1.display(0, 0)

    obj2 = LetterFactor().create_letter('t')
    obj2.display(0, 6)


if __name__ == "__main__":
    main()
