from Design_patterns.adapter.shape import Shape


class Square(Shape):

    def draw(self):
        print("Drawing Square")

    def resize(self):
        print("Resizing Square")