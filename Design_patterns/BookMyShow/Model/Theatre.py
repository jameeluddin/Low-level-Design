
class Theatre:

    def __init__(self, id, name, screens=None):
        self.id = id
        self.name = name
        self.screens = [] if screens is None else screens

    def add_screen(self, screen):
        self.screens.append(screen)
