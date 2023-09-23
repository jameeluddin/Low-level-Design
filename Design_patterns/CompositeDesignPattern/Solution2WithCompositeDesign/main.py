from Design_patterns.CompositeDesignPattern.Solution2WithCompositeDesign.Expression import Expression
from Design_patterns.CompositeDesignPattern.Solution2WithCompositeDesign.number import Number
from Design_patterns.CompositeDesignPattern.Solution2WithCompositeDesign.operation import Operation


def main():
    two = Number(2)
    one = Number(1)
    seven = Number(7)

    add_expression = Expression(one, seven, Operation.ADD)
    parent_expression = Expression(two, add_expression, Operation.MULTIPLY)
    print(parent_expression.evaluate())


if __name__ == "__main__":
    main()
