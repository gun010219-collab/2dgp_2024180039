# 실습 과제 진행
from pico2d import *

# 맨 처음 해야하는 일
open_canvas(800, 600)
boy = load_image('character.png')

def move_circle():
    print('CIRCLE')
# 캐릭터 이미지 표시
    boy.draw(400, 300)
    update_canvas()
    pass

def move_rectangle():
    print('RECTANGLE')
    pass

def move_triangle():
    print('TRIANGLE')
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

