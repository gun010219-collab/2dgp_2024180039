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
# SPIN
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
# ROLL
# ==================================================

roll_frames = [
    (1,   292, 30, 27),
    (36,  292, 29, 27),
    (70,  292, 29, 27),
    (105, 292, 29, 27),
    (139, 292, 29, 27),
    (174, 292, 29, 27)
]


# ==================================================
# MOTION 5
# ==================================================

motion_5_frames = [
    (1,   251, 29, 36),
    (36,  251, 30, 36),
    (74,  251, 31, 36),
    (111, 251, 31, 36),
    (149, 251, 30, 36),
    (186, 251, 31, 36)
]


# ==================================================
# MOTION 6
# ==================================================

motion_6_frames = [
    (1,   207, 29, 35),
    (36,  207, 30, 35),
    (72,  207, 39, 35),
    (123, 207, 39, 35),
    (172, 207, 39, 35),
    (218, 207, 38, 35)
]


# ==================================================
# MOTION 7
# ==================================================

motion_7_frames = [
    (1,   154, 24, 45),
    (31,  154, 29, 44),
    (65,  154, 20, 44),
    (90,  155, 25, 43),
    (119, 155, 25, 43),
    (149, 154, 20, 44),
    (184, 156, 40, 28),
    (232, 157, 39, 27)
]


# ==================================================
# MOTION 8
# ==================================================

motion_8_frames = [
    (1,   108, 27, 40),
    (31,  108, 31, 40),
    (64,  108, 31, 40),
    (99,  108, 33, 40),
    (136, 108, 32, 40),
    (176, 108, 33, 40),
    (217, 108, 33, 40),
    (254, 108, 33, 40)
]


# ==================================================
# MOTION 9
# ==================================================

motion_9_frames = [
    (6,   56, 34, 40),
    (49,  56, 34, 43),
    (96,  59, 23, 39),
    (125, 59, 23, 39)
]


# ==================================================
# MOTION 10
# ==================================================

motion_10_frames = [
    (1,   361, 33, 43),
    (39,  361, 35, 43),
    (89,  361, 35, 43),
    (130, 361, 34, 43),
    (181, 361, 34, 43),
    (228, 361, 33, 43)
]


# ==================================================
# 모든 애니메이션 무한 반복
# ==================================================

while True:

    # IDLE - 5회
    for repeat in range(5):
        for left, bottom, width, height in idle_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.1)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # RUN - 5회
    for repeat in range(5):
        for left, bottom, width, height in run_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # SPIN - 5회
    for repeat in range(5):
        for left, bottom, width, height in spin_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ROLL - 5회
    for repeat in range(5):
        for left, bottom, width, height in roll_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # MOTION 5 - 5회
    for repeat in range(5):
        for left, bottom, width, height in motion_5_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # MOTION 6 - 5회
    for repeat in range(5):
        for left, bottom, width, height in motion_6_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # MOTION 7 - 5회
    for repeat in range(5):
        for left, bottom, width, height in motion_7_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # MOTION 8 - 5회
    for repeat in range(5):
        for left, bottom, width, height in motion_8_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # MOTION 9 - 5회
    for repeat in range(5):
        for left, bottom, width, height in motion_9_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # MOTION 10 - 5회
    for repeat in range(5):
        for left, bottom, width, height in motion_10_frames:
            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, 300,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.08)


    # 마지막 1초 Idle
    clear_canvas()
    left, bottom, width, height = idle_frames[0]

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)