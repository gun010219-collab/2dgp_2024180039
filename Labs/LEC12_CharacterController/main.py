from pico2d import *

from grass import Grass
from boy import Boy


def handle_events():
    global running

    event_list = get_events()

    for event in event_list:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        else:
            boy.handle_event(event)


def reset_world():
    global world
    global boy

    world = []

    grass = Grass()
    world.append(grass)

    boy = Boy()
    world.append(boy)


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()


running = True

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()