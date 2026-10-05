from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')


# ==================================================
# IDLE
# ==================================================

idle_frames = [
    (1,   447, 29, 39),
    (31,  447, 26, 38),
    (58,  447, 29, 39),
    (88,  447, 28, 38),
    (118, 447, 30, 38),
    (150, 447, 30, 38),
    (181, 445, 30, 40)
]


# ==================================================
# RUN
# ==================================================

run_frames = [
    (8,   407, 26, 39),
    (37,  407, 27, 39),
    (65,  407, 31, 39),
    (97,  407, 37, 39),
    (135, 407, 32, 39),
    (170, 407, 32, 39),
    (206, 407, 26, 39),
    (238, 407, 24, 39),
    (263, 407, 30, 39),
    (295, 407, 36, 39),
    (334, 407, 32, 39),
    (370, 407, 29, 39)
]


# ==================================================
# SPIN / ROLL
# 몸을 둥글게 말아서 회전하는 동작
# ==================================================

spin_frames = [
    (1,   325, 29, 33),
    (35,  325, 29, 33),
    (67,  325, 30, 33),
    (98,  325, 31, 33),
    (131, 325, 29, 33),
    (162, 325, 29, 33),
    (193, 325, 30, 33)
]


# ==================================================
# IDLE - 5회 반복
# ==================================================

for repeat in range(5):
    for left, bottom, width, height in idle_frames:
        clear_canvas()

        sonic.clip_draw(
            left,
            bottom,
            width,
            height,
            600,
            300,
            width * 4,
            height * 4
        )

        update_canvas()
        delay(0.1)


# 1초 동안 Idle
clear_canvas()

left, bottom, width, height = idle_frames[0]

sonic.clip_draw(
    left,
    bottom,
    width,
    height,
    600,
    300,
    width * 4,
    height * 4
)

update_canvas()
delay(1)


# ==================================================
# RUN - 5회 반복
# ==================================================

for repeat in range(5):
    for left, bottom, width, height in run_frames:
        clear_canvas()

        sonic.clip_draw(
            left,
            bottom,
            width,
            height,
            600,
            300,
            width * 4,
            height * 4
        )

        update_canvas()
        delay(0.08)


# 1초 동안 Idle
clear_canvas()

left, bottom, width, height = idle_frames[0]

sonic.clip_draw(
    left,
    bottom,
    width,
    height,
    600,
    300,
    width * 4,
    height * 4
)

update_canvas()
delay(1)


# ==================================================
# SPIN / ROLL - 5회 반복
# ==================================================

for repeat in range(5):
    for left, bottom, width, height in spin_frames:
        clear_canvas()

        sonic.clip_draw(
            left,
            bottom,
            width,
            height,
            600,
            300,
            width * 4,
            height * 4
        )

        update_canvas()
        delay(0.08)


# 1초 동안 Idle
clear_canvas()

left, bottom, width, height = idle_frames[0]

sonic.clip_draw(
    left,
    bottom,
    width,
    height,
    600,
    300,
    width * 4,
    height * 4
)

update_canvas()
delay(1)

close_canvas()