from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global dir_x, dir_y
    global face_dir

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                face_dir = 1

            elif event.key == SDLK_LEFT:
                dir_x -= 1
                face_dir = -1

            elif event.key == SDLK_UP:
                dir_y += 1

            elif event.key == SDLK_DOWN:
                dir_y -= 1

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1

            elif event.key == SDLK_LEFT:
                dir_x += 1

            elif event.key == SDLK_UP:
                dir_y -= 1

            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True

x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2

frame = 0

dir_x = 0
dir_y = 0

# 1 = 오른쪽, -1 = 왼쪽
face_dir = 1


while running:
    clear_canvas()

    tuk_ground.draw(
        TUK_WIDTH // 2,
        TUK_HEIGHT // 2
    )


    # ==================================================
    # 정지 상태 - IDLE
    # ==================================================

    if dir_x == 0 and dir_y == 0:

        if face_dir == 1:
            # 1행 : 오른쪽 IDLE
            character.clip_draw(
                frame * 100,
                300,
                100,
                100,
                x,
                y
            )

        else:
            # 2행 : 왼쪽 IDLE
            character.clip_draw(
                frame * 100,
                200,
                100,
                100,
                x,
                y
            )


    # ==================================================
    # 이동 상태 - RUN
    # ==================================================

    else:

        if face_dir == 1:
            # 3행 : 오른쪽 RUN
            character.clip_draw(
                frame * 100,
                100,
                100,
                100,
                x,
                y
            )

        else:
            # 4행 : 왼쪽 RUN
            character.clip_draw(
                frame * 100,
                0,
                100,
                100,
                x,
                y
            )


    update_canvas()

    handle_events()


    # ==================================================
    # 캐릭터 이동
    # ==================================================

    x += dir_x * 5
    y += dir_y * 5


    # ==================================================
    # 화면 경계 제한
    # 캐릭터 크기가 100 x 100이므로 중심 기준 50px 확보
    # ==================================================

    if x < 50:
        x = 50

    elif x > TUK_WIDTH - 50:
        x = TUK_WIDTH - 50


    if y < 50:
        y = 50

    elif y > TUK_HEIGHT - 50:
        y = TUK_HEIGHT - 50


    # ==================================================
    # 애니메이션 프레임
    # ==================================================

    frame = (frame + 1) % 8

    delay(0.05)


close_canvas()