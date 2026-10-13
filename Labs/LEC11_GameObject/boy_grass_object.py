from pico2d import *
import random


# Game object class here

# 게임 객체를 파악.
# boy, grass, zombie 필요

class Grass:  # 클래스는 대문자로 시작한다
    # 잔디 속성을 초기화
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self, speed=5):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.speed = speed
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed

    def draw(self):
        self.image.clip_draw(
            self.frame * 100, 0, 100, 100,
            self.x, self.y
        )


class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h

        self.image.clip_draw(
            self.frame * frame_width, 0,
            frame_width, frame_height,
            self.x, self.y,
            frame_width // 2, frame_height // 2
        )

class Ball:
    def __init__(self):
        self.x = random.randint(30,599)
        self.y = random.randint(400,599)
        self.speed = random.randint(10,30)
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -=self.speed
        if self.y < 20:
            self.x = random.randint(20,599)
            self.y = random.randint(599,30)

    def draw(self):
        self.image.draw(self.x,self.y)

def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global world

    running = True
    world = []

    # 잔디 객체 생성
    grass = Grass()
    world.append(grass)

    # 소년 객체 11명 생성 (List Comprehension)
    team = [Boy() for i in range(11)]
    world += team

    # 좀비 객체 생성
    zombie = Zombie()
    world.append(zombie)

    # ball 객체 20개 생성
    ball = [Ball() for i in range(20)]
    world += ball


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()


open_canvas()

reset_world()  # 세상을 구성하는 객체들을 초기화

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()