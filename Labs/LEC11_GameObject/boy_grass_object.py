from pico2d import *
import random


# Game object class here

# 게임 객체를 파악.
# boy, grass 필요

class Grass:  # 클래스는 대문자로 시작한다
    # 잔디 속성을 초기화
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    running = True

    # 잔디 객체를 찍어낸다
    global grass
    grass = Grass()

    # 소년 객체를 찍어낸다
    global boy
    boy = Boy()


def update_world():
    global grass, boy
    grass.update()
    boy.update()


def render_world():
    global grass, boy
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


open_canvas()

reset_world()  # 세상을 구성하는 객체들을 초기화

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()