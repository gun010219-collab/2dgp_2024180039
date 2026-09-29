from pico2d import *

open_canvas()

idle = load_image('Idle.png')

idle.clip_draw(
    0, 0, 160, 160,
    400, 300,
    320, 320
)

update_canvas()
delay(2)

close_canvas()