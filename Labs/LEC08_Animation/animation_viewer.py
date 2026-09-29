from pico2d import *

open_canvas()

idle = load_image('Idle.png')

frame = 0

for repeat in range(5):
    for i in range(8):
        clear_canvas()

        idle.clip_draw(
            0, frame * 160, 160, 160,
            400, 300,
            320, 320
        )

        update_canvas()

        frame = (frame + 1) % 8
        delay(0.1)

close_canvas()