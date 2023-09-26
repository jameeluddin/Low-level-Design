from Design_patterns.FlyWeightPattern.wordProcessor.ILetter import ILetter


class DocumentCharacter(ILetter):
    def __init__(self, char, font_type, size):
        self.char = char
        self.font_type = font_type
        self.size = size

    def display(self, row, col):
        pass
