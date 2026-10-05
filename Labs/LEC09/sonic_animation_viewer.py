from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

clear_canvas()

# 첫 번째 소닉 프레임 출력
sonic.clip_draw(
    5, 455,
    25, 35,
    600, 300,
    100, 140
)

update_canvas()

delay(3)

close_canvas()