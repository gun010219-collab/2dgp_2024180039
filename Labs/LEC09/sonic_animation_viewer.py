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

    # ==================================================
    # IDLE - 5회
    # ==================================================

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


    # IDLE 마지막 프레임에서 1초 정지
    left, bottom, width, height = idle_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # RUN - 5회
    # 좌우 이동 + 경계에서 방향 반전
    # ==================================================

    run_x = 100
    run_speed = 20

    last_run_frame = run_frames[0]

    for repeat in range(5):
        for left, bottom, width, height in run_frames:

            clear_canvas()

            # 오른쪽 이동
            if run_speed > 0:
                sonic.clip_draw(
                    left, bottom,
                    width, height,
                    run_x, 300,
                    width * 4, height * 4
                )

            # 왼쪽 이동
            else:
                sonic.clip_composite_draw(
                    left, bottom,
                    width, height,
                    0, 'h',
                    run_x, 300,
                    width * 4, height * 4
                )

            update_canvas()
            delay(0.08)

            last_run_frame = (left, bottom, width, height)

            run_x += run_speed

            # 오른쪽 경계
            if run_x >= 1100:
                run_x = 1100
                run_speed = -20

            # 왼쪽 경계
            elif run_x <= 100:
                run_x = 100
                run_speed = 20


    # RUN 종료 위치에서 1초 정지
    left, bottom, width, height = last_run_frame

    clear_canvas()

    if run_speed > 0:
        sonic.clip_draw(
            left, bottom,
            width, height,
            run_x, 300,
            width * 4, height * 4
        )

    else:
        sonic.clip_composite_draw(
            left, bottom,
            width, height,
            0, 'h',
            run_x, 300,
            width * 4, height * 4
        )

    update_canvas()
    delay(1)


    # ==================================================
    # SPIN / JUMP - 5회
    # 회전하면서 상승 후 하강
    # ==================================================

    last_spin_frame = spin_frames[0]

    for repeat in range(5):

        frame_index = 0

        # 상승
        for jump_y in range(300, 501, 20):

            left, bottom, width, height = spin_frames[
                frame_index % len(spin_frames)
            ]

            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, jump_y,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.05)

            last_spin_frame = (left, bottom, width, height)

            frame_index += 1


        # 하강
        for jump_y in range(500, 299, -20):

            left, bottom, width, height = spin_frames[
                frame_index % len(spin_frames)
            ]

            clear_canvas()

            sonic.clip_draw(
                left, bottom,
                width, height,
                600, jump_y,
                width * 4, height * 4
            )

            update_canvas()
            delay(0.05)

            last_spin_frame = (left, bottom, width, height)

            frame_index += 1


    # 점프 종료 위치에서 1초 정지
    left, bottom, width, height = last_spin_frame

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # ROLL - 5회
    # ==================================================

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


    left, bottom, width, height = roll_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # MOTION 5 - 5회
    # ==================================================

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


    left, bottom, width, height = motion_5_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # MOTION 6 - 5회
    # ==================================================

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


    left, bottom, width, height = motion_6_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # MOTION 7 - 5회
    # ==================================================

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


    left, bottom, width, height = motion_7_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # MOTION 8 - 5회
    # ==================================================

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


    left, bottom, width, height = motion_8_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # MOTION 9 - 5회
    # ==================================================

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


    left, bottom, width, height = motion_9_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)


    # ==================================================
    # MOTION 10 - 5회
    # ==================================================

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


    left, bottom, width, height = motion_10_frames[-1]

    clear_canvas()

    sonic.clip_draw(
        left, bottom,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()
    delay(1)