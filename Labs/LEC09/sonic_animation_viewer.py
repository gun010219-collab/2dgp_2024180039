from pico2d import *


open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')


# ==================================================
# IDLE
# 11 Frames
# ==================================================

idle_frames = [
    (1,   447, 29, 39),
    (31,  447, 26, 38),
    (58,  447, 29, 39),
    (88,  447, 28, 38),
    (118, 447, 30, 38),
    (150, 447, 30, 38),
    (181, 445, 30, 40),

    # 누락 프레임 보완
    (211, 448, 29, 38),
    (240, 448, 29, 38),
    (270, 448, 24, 32),
    (302, 448, 29, 26)
]


# ==================================================
# RUN
# 12 Frames
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
# 9 Frames
# ==================================================

spin_frames = [
    (1,   325, 29, 33),
    (35,  325, 29, 33),
    (67,  325, 30, 33),
    (98,  325, 31, 33),
    (131, 325, 29, 33),
    (162, 325, 29, 33),
    (193, 325, 30, 33),

    # 누락 프레임 보완
    (230, 326, 31, 29),
    (268, 325, 30, 30)
]


# ==================================================
# ROLL
# 6 Frames
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
# 6 Frames
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
# 6 Frames
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
# 8 Frames
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
# 8 Frames
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
# 4 Frames
# ==================================================

motion_9_frames = [
    (6,   56, 34, 40),
    (49,  56, 34, 43),
    (96,  59, 23, 39),
    (125, 59, 23, 39)
]


# ==================================================
# MOTION 10
# 6 Frames
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
# 프레임 개수 검증
# ==================================================

all_animations = [
    idle_frames,
    run_frames,
    spin_frames,
    roll_frames,
    motion_5_frames,
    motion_6_frames,
    motion_7_frames,
    motion_8_frames,
    motion_9_frames,
    motion_10_frames
]

total_frames = sum(
    len(frames)
    for frames in all_animations
)

assert total_frames == 76


# ==================================================
# 이벤트 처리
# ==================================================

def check_events():
    for event in get_events():

        if event.type == SDL_QUIT:
            raise SystemExit

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                raise SystemExit


# ==================================================
# 이벤트를 처리하면서 대기
# ==================================================

def wait_with_events(seconds):

    elapsed = 0.0

    while elapsed < seconds:

        check_events()

        wait_time = min(
            0.01,
            seconds - elapsed
        )

        delay(wait_time)

        elapsed += wait_time


# ==================================================
# 프레임 출력
# ==================================================

def draw_frame(frame, x, y, flip=False):

    left, bottom, width, height = frame

    clear_canvas()

    if flip:

        sonic.clip_composite_draw(
            left,
            bottom,
            width,
            height,
            0,
            'h',
            x,
            y,
            width * 4,
            height * 4
        )

    else:

        sonic.clip_draw(
            left,
            bottom,
            width,
            height,
            x,
            y,
            width * 4,
            height * 4
        )

    update_canvas()


# ==================================================
# 제자리 애니메이션
# ==================================================

def play_stationary(frames, frame_delay=0.08):

    for repeat in range(5):

        for frame in frames:

            draw_frame(
                frame,
                600,
                300
            )

            wait_with_events(
                frame_delay
            )


    # 마지막 프레임 유지
    draw_frame(
        frames[-1],
        600,
        300
    )

    wait_with_events(1.0)


# ==================================================
# RUN
# 좌우 이동
# ==================================================

def play_run():

    run_x = 100
    run_speed = 20

    last_frame = run_frames[0]
    last_x = run_x
    last_flip = False


    for repeat in range(5):

        for frame in run_frames:

            flip = run_speed < 0

            draw_frame(
                frame,
                run_x,
                300,
                flip
            )

            wait_with_events(0.08)


            # 마지막 화면 상태 저장
            last_frame = frame
            last_x = run_x
            last_flip = flip


            # 위치 이동
            run_x += run_speed


            # 오른쪽 경계
            if run_x >= 1100:

                run_x = 1100
                run_speed = -20


            # 왼쪽 경계
            elif run_x <= 100:

                run_x = 100
                run_speed = 20


    # 마지막 위치와 방향 그대로 1초 유지
    draw_frame(
        last_frame,
        last_x,
        300,
        last_flip
    )

    wait_with_events(1.0)


# ==================================================
# SPIN / JUMP
# 상승 후 하강
# ==================================================

def play_jump():

    last_frame = spin_frames[-1]


    for repeat in range(5):

        frame_count = len(spin_frames)


        for i, frame in enumerate(spin_frames):

            # 0.0 ~ 1.0
            t = i / (frame_count - 1)


            # 포물선 형태
            jump_y = 300 + int(
                200 * 4 * t * (1 - t)
            )


            draw_frame(
                frame,
                600,
                jump_y
            )

            wait_with_events(0.08)

            last_frame = frame


    # 점프 종료 위치에서 1초 정지
    draw_frame(
        last_frame,
        600,
        300
    )

    wait_with_events(1.0)


# ==================================================
# 전체 애니메이션 재생
# ==================================================

try:

    while True:

        # IDLE
        play_stationary(
            idle_frames,
            0.1
        )


        # RUN
        play_run()


        # SPIN / JUMP
        play_jump()


        # ROLL
        play_stationary(
            roll_frames
        )


        # MOTION 5
        play_stationary(
            motion_5_frames
        )


        # MOTION 6
        play_stationary(
            motion_6_frames
        )


        # MOTION 7
        play_stationary(
            motion_7_frames
        )


        # MOTION 8
        play_stationary(
            motion_8_frames
        )


        # MOTION 9
        play_stationary(
            motion_9_frames
        )


        # MOTION 10
        play_stationary(
            motion_10_frames
        )


finally:

    close_canvas()