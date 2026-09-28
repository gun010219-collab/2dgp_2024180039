from pico2d import *
import math

WIDTH = 800
HEIGHT = 600
FRAME_DELAY = 0.01

open_canvas(WIDTH, HEIGHT)
character = load_image('character.png')


def render(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def circle_motion():
    center_x = 400
    center_y = 300
    radius = 200

    for degree in range(360):
        angle = math.radians(degree)

        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        render(x, y)


def move_line(start_x, start_y, end_x, end_y, frames=120):
    for frame in range(frames + 1):
        ratio = frame / frames

        x = start_x + (end_x - start_x) * ratio
        y = start_y + (end_y - start_y) * ratio

        render(x, y)


def rectangle_motion():
    points = [
        (50, 550),
        (750, 550),
        (750, 50),
        (50, 50),
        (50, 550)
    ]

    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]

        move_line(start[0], start[1], end[0], end[1])


def triangle_motion():
    points = [
        (100, 100),
        (700, 100),
        (400, 500),
        (100, 100)
    ]

    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]

        move_line(start[0], start[1], end[0], end[1])


while True:
    circle_motion()
    rectangle_motion()
    triangle_motion()