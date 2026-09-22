from pico2d import *


open_canvas(1000, 1000)

character = load_image('character.png')

character.draw(400, 300)
character.draw(300, 200)
character.draw(500, 400)
for x in range(0, 9):
    for y in range(0, 7):
        character.draw(x * 100, y * 100)

update_canvas()
delay(2)
close_canvas()