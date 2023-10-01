from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def draw_line(x1, y1, x2, y2):
    global startx, starty
    global x,y
    global t
    global handx, handy

    t += 0.001
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2
    if t > 1.0:
        handx, handy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
        startx , starty = x, y
        t = 0

def  decide_direction():
    global direction
    if handx < x:
        direction = 0
    else:
        direction = 1


running = True
startx, starty = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = startx, starty
direction = 0
frame = 0
t = 0
hide_cursor()
handx , handy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    decide_direction()
    draw_line(startx, starty, handx, handy)
    hand_arrow.draw(handx, handy)
    character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




