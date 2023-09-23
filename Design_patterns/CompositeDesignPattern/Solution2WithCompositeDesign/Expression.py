from Design_patterns.CompositeDesignPattern.Solution2WithCompositeDesign.ArithmeticExpression import ArithmeticExpression
from Design_patterns.CompositeDesignPattern.Solution2WithCompositeDesign.operation import Operation


class Expression(ArithmeticExpression):
    def __init__(self, left_part, right_part, operation):
        self.left_part = left_part
        self.right_part = right_part
        self.operation = operation

    def evaluate(self):
        value = 0
        if self.operation == Operation.ADD:
            value = self.left_part.evaluate() + self.right_part.evaluate()
        elif self.operation == Operation.SUBTRACT:
            value = self.left_part.evaluate() - self.right_part.evaluate()
        elif self.operation == Operation.DIVIDE:
            value = self.left_part.evaluate() / self.right_part.evaluate()
        elif self.operation == Operation.MULTIPLY:
            value = self.left_part.evaluate() * self.right_part.evaluate()

        print("Expression value is :", value)

        return value
