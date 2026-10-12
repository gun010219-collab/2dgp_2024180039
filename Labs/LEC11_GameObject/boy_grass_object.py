from pico2d import *
import random


# Game object class here

# 게임 객체를 파악.
# boy, grass 필요

class Grass: # 클래스는 대문자로 시작한다
    # 잔디 속성을 초기화
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass
    


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


def update_world():
    global grass
    grass.update()
    pass


def render_world():
    global grass
    clear_canvas()
    grass.draw()
    update_canvas()


open_canvas()

reset_world() # 세상을 구성하는 객체들을 초기화

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()