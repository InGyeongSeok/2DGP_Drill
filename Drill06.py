from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global handx, handy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            handx, handy = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            point_x, point_y = event.x, TUK_HEIGHT - 1 - event.y
            hand_point.append((point_x, point_y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



running = True
startx, starty = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = startx, starty
handx, handy = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
t = 0
hide_cursor()
hand_point = []

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(handx, handy)
    for arr in hand_point:
        hand_arrow.draw(arr[0], arr[1])

    if len(hand_point) == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8

    elif hand_point and t < 1:
        t += 0.002
        x = (1 - t) * startx + t * hand_point[0][0]
        y = (1 - t) * starty + t * hand_point[0][1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8

    if t > 1:
        startx = x
        starty = y
        del hand_point[0]
        t = 0

    update_canvas()
    handle_events()

close_canvas()




