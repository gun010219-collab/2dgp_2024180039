from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

clear_canvas()

sonic.draw(600, 300)

update_canvas()

delay(3)

close_canvas()