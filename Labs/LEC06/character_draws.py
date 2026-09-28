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

def draw_top():
    print('TOP')
    for x in range(50, 750, 5):
        draw_character(x)
    pass

def draw_character(x):
    clear_canvas()
    boy.draw(x, 550)
    update_canvas()
    delay(0.01)

def draw_right():
    print('RIGHT')
    pass

def draw_bottom():
    print('BOTTOM')
    pass

def draw_left():
    print('LEFT')
    pass

def move_rectangle():
    print('RECTANGLE')
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def move_triangle():
    print('TRIANGLE')
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass