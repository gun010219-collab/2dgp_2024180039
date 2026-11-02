from pico2d import load_image


class Grass:
    def __init__(self, y = 30):
        self.image = load_image('grass.png')
        self.y = y

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
