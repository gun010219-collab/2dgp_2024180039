from pico2d import *
import random


# Game object class here

# 게임 객체를 파악.
# boy, grass 필요

class Grass:
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


def update_world():
    pass


def render_world():
    clear_canvas()
    update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()