from pico2d import *

open_canvas()

idle = load_image('Idle.png')
walk = load_image('Walk.png')
jump = load_image('Jump.png')
attack = load_image('Attack 1.png')

while True:
    frame = 0

    for repeat in range(5):
        for i in range(8):
            clear_canvas()

            idle.clip_draw(
                0, frame * 160, 160, 160,
                400, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 8
            delay(0.1)

    delay(1)

    frame = 0

    for repeat in range(5):
        for i in range(10):
            clear_canvas()

            walk.clip_draw(
                0, frame * 160, 160, 160,
                400, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 10
            delay(0.1)

    delay(1)

    frame = 0

    for repeat in range(5):
        for i in range(4):
            clear_canvas()

            jump.clip_draw(
                0, frame * 160, 160, 160,
                400, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 4
            delay(0.1)

    delay(1)

    frame = 0

    for repeat in range(5):
        for i in range(8):
            clear_canvas()

            attack.clip_draw(
                0, frame * 160, 160, 160,
                400, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 8
            delay(0.1)

    delay(1)

close_canvas()