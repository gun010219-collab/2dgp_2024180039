from pico2d import *
from boy import Boy
from grass import Grass
from ball import Ball

import game_world

# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if boy.state != 'SLEEP':
                game_world.add_object(
                    Ball(boy.x + boy.face_dir * 35, boy.y - 30, boy.face_dir)
                )
            boy.handle_event(event)
        else:
            boy.handle_event(event)



def reset_world():
    global world
    global boy

    grass = Grass()
    game_world.add_object(grass)

    boy = Boy()
    game_world.add_object(boy)



def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.rander()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
