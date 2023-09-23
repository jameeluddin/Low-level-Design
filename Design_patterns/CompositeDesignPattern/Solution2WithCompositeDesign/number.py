from Design_patterns.CompositeDesignPattern.Solution2WithCompositeDesign.ArithmeticExpression import ArithmeticExpression


class Number(ArithmeticExpression):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        print("Number value is :", self.value)
        return self.value