from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    def __init__(self, x, y, direction=1):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * self.speed
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
