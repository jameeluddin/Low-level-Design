
class DrawService:
    shapes = []

    def add_shapes(self, shape):
        self.shapes.append(shape)


    def get_shapes(self):
        return self.shapes

    def draw(self):
        if len(self.shapes) == 0:
            print("Nothing to draw")
        else:
            for shape in self.shapes:
                shape.draw()

    def resize(self):
        if len(self.shapes) == 0:
            print("Nothing to draw")
        else:
            for shape in self.shapes:
                shape.resize()
