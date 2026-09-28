from pico2d import *
import math

# 맨 처음 해야하는 일
open_canvas(800, 600)
boy = load_image('character.png')

def move_circle():
    print('CIRCLE')

    degree = 0

    while degree < 360:
        clear_canvas()

        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        boy.draw(x, y)
        update_canvas()

        degree += 1
        delay(0.01)

def move_top():
    print('top')
    pass

def move_right():
    print('right')
    pass

def move_bottom():
    print('bottom')
    pass

def move_left():
    print('left')
    pass


def move_rectangle():
    print('RECTANGLE')
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_triangle():
    print('TRIANGLE')
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass