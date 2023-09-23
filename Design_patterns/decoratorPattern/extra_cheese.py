from Design_patterns.decoratorPattern.topping_decorator import ToppingDecorator


class ExtraCheese(ToppingDecorator):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 10
