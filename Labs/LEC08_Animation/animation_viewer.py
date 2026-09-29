from pico2d import *

open_canvas()

idle = load_image('Idle.png')
walk = load_image('Walk.png')
jump = load_image('Jump.png')
attack = load_image('Attack 1.png')


# 1초 동안 Idle 애니메이션 재생
def play_idle_1_second():
    frame = 0

    for i in range(10):
        clear_canvas()

        idle.clip_draw(
            0, frame * 160, 160, 160,
            400, 300,
            400, 400
        )

        update_canvas()

        frame = (frame + 1) % 8
        delay(0.1)


while True:
    frame = 0

    # Idle
    for repeat in range(5):
        for i in range(8):
            clear_canvas()

            idle.clip_draw(
                0, frame * 160, 160, 160,
                400, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 8
            delay(0.1)

    play_idle_1_second()

    frame = 0

    # Walk
    for repeat in range(5):

        # 왼쪽 -> 오른쪽
        for x in range(100, 701, 15):
            clear_canvas()

            walk.clip_draw(
                0, frame * 160, 160, 160,
                x, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 10
            delay(0.03)

        # 오른쪽 -> 왼쪽
        for x in range(700, 99, -15):
            clear_canvas()

            walk.clip_composite_draw(
                0, frame * 160, 160, 160,
                0, 'h',
                x, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 10
            delay(0.03)

    play_idle_1_second()

    frame = 0

    # Jump
    for repeat in range(5):
        for i in range(4):
            clear_canvas()

            jump.clip_draw(
                0, frame * 160, 160, 160,
                400, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 4
            delay(0.1)

    play_idle_1_second()

    frame = 0

    # Attack
    for repeat in range(5):
        for i in range(8):
            clear_canvas()

            attack.clip_draw(
                0, frame * 160, 160, 160,
                400, 300,
                400, 400
            )

            update_canvas()

            frame = (frame + 1) % 8
            delay(0.1)

    play_idle_1_second()

close_canvas()