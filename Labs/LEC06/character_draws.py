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
        draw_character(x, 550)
    pass

def draw_character(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_right():
    print('RIGHT')
    for y in range(550, 50, -5):
        draw_character(750, y)
        pass
      
def draw_bottom():
    print('BOTTOM')
    for x in range(750, 50, -5):
        draw_character(x, 50)
        pass

def draw_left():
    print('LEFT')
    for y in range(50, 550, 5):
        draw_character(50, y)
        pass

def move_rectangle():
    print('RECTANGLE')
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def draw_triangle_1():
    print('TRIANGLE 1')
    for x in range(100, 700, 5):
        draw_character(x, 100)
        pass

def draw_triangle_2():
    print('TRIANGLE 2')
    for step in range(101):
        t = step / 100
        x = 700 + (400 - 700) * t
        y = 100 + (500 - 100) * t
        draw_character(x, y)
        pass

def draw_triangle_3():
    print('TRIANGLE 3')
    for step in range(101):
        pass

def move_triangle():
    print('TRIANGLE')
    draw_triangle_1()
    draw_triangle_2()
    draw_triangle_3()
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass