from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('jake.png')


def handle_events():
    global running, dirx, diry

    # fill here
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1



running = True
x, y = 100, 230
frame = 0
dirx = 0
diry = 0


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)

    if dirx == 0 and diry == 0: #IDLE
        character.clip_draw(frame * 25 + 10, 326, 27, 50, x, y, 100, 100)
        frame = (frame + 1) % 3
        delay(0.1)

    if dirx > 0 and diry == 0: # RIGHT
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 280, 27, 50, x, y, 100, 100)
        if frame == 3:
            character.clip_draw(frame * 25 + 20, 285, 35, 49, x, y, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 285, 36, 49, x, y, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28,  285, 30, 49, x, y, 100, 100)
        if frame == 6:
            character.clip_draw(frame * 28 + 28,  285, 30, 49, x, y, 100, 100)
        frame = (frame + 1) % 7
        if x < TUK_WIDTH - 50:
            x += dirx * 10
        delay(0.1)

    if dirx < 0 and diry == 0: # LEFT
        if frame <= 2:
            character.clip_composite_draw(frame * 25 + 10, 280, 27, 50, 0, 'h', x, y, 100, 100)
        if frame == 3:
            character.clip_composite_draw(frame * 25 + 20, 285, 35, 49, 0, 'h',x, y, 100, 100)
        if frame == 4:
            character.clip_composite_draw(frame * 28 + 20, 285, 36, 49, 0, 'h',x, y, 100, 100)
        if frame == 5:
            character.clip_composite_draw(frame * 28 + 28,  285, 30, 49,0, 'h', x, y, 100, 100)
        if frame == 6:
            character.clip_composite_draw(frame * 28 + 28,  285, 30, 49,0, 'h',x, y, 100, 100)
        frame = (frame + 1) % 7
        if x > 50:
            x += dirx * 10
        delay(0.1)

    if dirx == 0 and diry > 0: # UP
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 190, 27, 50, x, y, 100, 100)
        if frame == 3:
            character.clip_draw(frame * 25 + 20, 190, 35, 49, x, y, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 190, 36, 49, x, y, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28,  190, 30, 49, x, y, 100, 100)
        if frame == 6:
            character.clip_draw(frame * 28 + 28,  190, 30, 49, x, y, 100, 100)
        frame = (frame + 1) % 7
        if y < TUK_HEIGHT - 50:
            y += diry * 10
        delay(0.1)

    if dirx == 0 and diry < 0: # DOWN
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 326, 27, 50, x, y, 100, 100)
        if frame == 3:
            character.clip_draw(frame * 25 + 20, 326, 35, 49, x, y, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 330, 36, 49, x, y, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28,  326, 30, 49, x, y, 100, 100)
        if frame == 6:
            character.clip_draw(frame * 28 + 28,  326, 30, 49, x, y, 100, 100)
        frame = (frame + 1) % 7
        if y > 50:
            y += diry * 10
        delay(0.1)

    if dirx > 0 and diry > 0: # UP &  RIGHT
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 190, 27, 50, x, y, 100, 100)
        if frame == 3:
            character.clip_draw(frame * 25 + 20, 190, 35, 49, x, y, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 190, 36, 49, x, y, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28, 190, 30, 49, x, y, 100, 100)
        if frame == 6:
            character.clip_draw(frame * 28 + 28, 190, 30, 49, x, y, 100, 100)
        frame = (frame + 1) % 7
        if x < TUK_WIDTH - 50 and y < TUK_HEIGHT - 50:
            x += dirx * 10
            y += diry * 10
        delay(0.1)

    if dirx < 0 and diry > 0: # UP & LEFT
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 190, 27, 50, x, y, 100, 100)
        if frame == 3:
            character.clip_draw(frame * 25 + 20, 190, 35, 49, x, y, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 190, 36, 49, x, y, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28, 190, 30, 49, x, y, 100, 100)
        if frame == 6:
            character.clip_draw(frame * 28 + 28, 190, 30, 49, x, y, 100, 100)
        frame = (frame + 1) % 7
        if x > 50 and y < TUK_HEIGHT - 50:
            x += dirx * 10
            y += diry * 10
        delay(0.1)

    if dirx < 0 and diry < 0: # DOWN & LEFT
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 326, 27, 50, x, y, 100, 100)
        if frame == 3:
            character.clip_draw(frame * 25 + 20, 326, 35, 49, x, y, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 330, 36, 49, x, y, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28, 326, 30, 49, x, y, 100, 100)
        if frame == 6:
            character.clip_draw(frame * 28 + 28, 326, 30, 49, x, y, 100, 100)
        frame = (frame + 1) % 7
        if x > 50 and y > 50:
            x += dirx * 10
            y += diry * 10
        delay(0.1)

    if dirx > 0 and diry < 0: # DOWN & RIGHT
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 326, 27, 50, x, y, 100, 100)
        if frame == 3:
            character.clip_draw(frame * 25 + 20, 326, 35, 49, x, y, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 330, 36, 49, x, y, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28, 326, 30, 49, x, y, 100, 100)
        if frame == 6:
            character.clip_draw(frame * 28 + 28, 326, 30, 49, x, y, 100, 100)
        frame = (frame + 1) % 7
        if x < TUK_WIDTH - 50 and y > 50:
            x += dirx * 10
            y += diry * 10


        delay(0.1)
    update_canvas()
    handle_events()

close_canvas()