from Design_patterns.decoratorPattern.extra_cheese import ExtraCheese
from Design_patterns.decoratorPattern.margherita import Margherita
from Design_patterns.decoratorPattern.mushroom import Mushroom


def main():
    bef = Margherita()
    def1 = ExtraCheese(bef)

    print(def1.cost())

    def2 = Mushroom(bef)
    print(def2.cost())


if __name__ == "__main__":
    main()
