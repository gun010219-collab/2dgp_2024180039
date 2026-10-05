from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')


# 첫 번째 동작의 프레임 영역
# (left, bottom, width, height)
frames = [
    (5, 455, 25, 35),
    (34, 455, 25, 35),
    (63, 455, 25, 35),
    (92, 455, 25, 35),
    (121, 455, 25, 35),
    (150, 455, 25, 35),
    (179, 455, 25, 35),
    (208, 455, 25, 35)
]


# 첫 번째 동작 5회 반복
for repeat in range(5):
    for left, bottom, width, height in frames:
        clear_canvas()

        sonic.clip_draw(
            left, bottom,
            width, height,
            600, 300,
            width * 4, height * 4
        )

        update_canvas()
        delay(0.1)


# 애니메이션 종료 후 1초 대기
delay(1)

close_canvas()