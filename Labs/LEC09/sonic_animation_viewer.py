from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')


# ==================================================
# IDLE
# 맨 위 행 왼쪽의 Idle 동작 7프레임
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
# 두 번째 행의 달리기 동작
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
# IDLE 5회 반복
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


# ==================================================
# 동작 사이 1초 대기
# 대기 중에는 Idle 첫 프레임 표시
# ==================================================

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
# RUN 5회 반복
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


# ==================================================
# 종료 전 Idle 상태로 1초 대기
# ==================================================

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