from pico2d import *
from transitions import Machine


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0.0
        self.face_dir = 1

        self.image = load_image('animation_sheet.png')

        self.left_pressed = False
        self.right_pressed = False

        self.speed = 250

        self.idle_start_time = get_time()
        self.last_update_time = get_time()

        self.machine = Machine(
            model=self,
            states=['IDLE', 'SLEEP', 'RUN'],
            initial='IDLE',
            transitions=[
                {
                    'trigger': 'go_sleep',
                    'source': 'IDLE',
                    'dest': 'SLEEP',
                    'after': 'enter_sleep'
                },
                {
                    'trigger': 'wake_up',
                    'source': 'SLEEP',
                    'dest': 'IDLE',
                    'after': 'enter_idle'
                },
                {
                    'trigger': 'start_run',
                    'source': ['IDLE', 'SLEEP'],
                    'dest': 'RUN',
                    'after': 'enter_run'
                },
                {
                    'trigger': 'stop_run',
                    'source': 'RUN',
                    'dest': 'IDLE',
                    'after': 'enter_idle'
                }
            ],
            auto_transitions=False
        )

        print('현재 상태: IDLE')

    def enter_idle(self):
        self.frame = 0
        self.idle_start_time = get_time()
        print('현재 상태: IDLE')

    def enter_sleep(self):
        self.frame = 0
        print('현재 상태: SLEEP')

    def enter_run(self):
        self.frame = 0
        print('현재 상태: RUN')

    def handle_event(self, event):

        if event.type == SDL_KEYDOWN:

            if event.key == SDLK_SPACE:
                if self.state == 'SLEEP':
                    self.wake_up()

            elif event.key == SDLK_RIGHT:
                self.right_pressed = True
                self.face_dir = 1

                if self.state != 'RUN':
                    self.start_run()

            elif event.key == SDLK_LEFT:
                self.left_pressed = True
                self.face_dir = -1

                if self.state != 'RUN':
                    self.start_run()

        elif event.type == SDL_KEYUP:

            if event.key == SDLK_RIGHT:
                self.right_pressed = False

            elif event.key == SDLK_LEFT:
                self.left_pressed = False

            if self.state == 'RUN':

                if self.right_pressed:
                    self.face_dir = 1

                elif self.left_pressed:
                    self.face_dir = -1

                else:
                    self.stop_run()

    def update(self):
        now = get_time()
        dt = max(0.0, min(now - self.last_update_time, 0.05))
        self.last_update_time = now

        if self.state == 'IDLE':
            self.frame = (self.frame + 8 * dt) % 8

            if now - self.idle_start_time >= 5.0:
                self.go_sleep()

        elif self.state == 'SLEEP':
            self.frame = 0

        elif self.state == 'RUN':
            self.frame = (self.frame + 12 * dt) % 8

            direction = (
                int(self.right_pressed)
                - int(self.left_pressed)
            )

            self.x += direction * self.speed * dt

            self.x = max(50, min(750, self.x))

    def draw(self):

        if self.state == 'RUN':
            sprite_y = 100 if self.face_dir == 1 else 0
            frame = int(self.frame)

        else:
            sprite_y = 300 if self.face_dir == 1 else 200

            if self.state == 'SLEEP':
                frame = 0
            else:
                frame = int(self.frame)

        self.image.clip_draw(
            frame * 100,
            sprite_y,
            100,
            100,
            self.x,
            self.y
        )