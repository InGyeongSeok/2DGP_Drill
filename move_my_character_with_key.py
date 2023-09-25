from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1000, 800
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
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dirx = 0
diry = 0



while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    #character.clip_draw( frame * 25 + 10, 0, 30, 60, 300, 300, 100, 100)

    # if dirx == 0 and diry == 0: #IDLE
    #     character.clip_draw(frame * 25 + 10, 326, 27, 50, 100, 400, 100, 100)
    #     frame = (frame + 1) % 3
    #     delay(0.1)
    #
    # if dirx > 0 and diry == 0: # RIGHT
    #     if frame <= 2:
    #         character.clip_draw(frame * 25 + 10, 280, 27, 50, 100, 400, 100, 100)
    #     if frame == 3:
    #         character.clip_draw(frame * 25 + 20, 285, 35, 49, 100, 400, 100, 100)
    #     if frame == 4:
    #         character.clip_draw(frame * 28 + 20, 285, 36, 49, 100, 400, 100, 100)
    #     if frame == 5:
    #         character.clip_draw(frame * 28 + 28,  285, 30, 49, 100, 400, 100, 100)
    #     if frame == 6:
    #         character.clip_draw(frame * 28 + 28,  285, 30, 49, 100, 400, 100, 100)
    #     frame = (frame + 1) % 7
    #     delay(0.1)
    #
    # if dirx < 0 and diry == 0: # LEFT
    #     if frame <= 2:
    #         character.clip_composite_draw(frame * 25 + 10, 280, 27, 50, 0, 'h', 100, 400, 100, 100)
    #     if frame == 3:
    #         character.clip_composite_draw(frame * 25 + 20, 285, 35, 49, 0, 'h',100, 400, 100, 100)
    #     if frame == 4:
    #         character.clip_composite_draw(frame * 28 + 20, 285, 36, 49, 0, 'h',100, 400, 100, 100)
    #     if frame == 5:
    #         character.clip_composite_draw(frame * 28 + 28,  285, 30, 49,0, 'h', 100, 400, 100, 100)
    #     if frame == 6:
    #         character.clip_composite_draw(frame * 28 + 28,  285, 30, 49,0, 'h', 100, 400, 100, 100)
    #     frame = (frame + 1) % 7
    #     delay(0.1)

    if dirx == 0 and diry > 0: # UP
        if frame <= 2:
            character.clip_draw(frame * 25 + 10, 190, 27, 50, 100, 400, 100, 100)
        if frame == 3:
            character.clip_draw(3 * 25 + 20, 190, 35, 49, 100, 400, 100, 100)
        if frame == 4:
            character.clip_draw(frame * 28 + 20, 190, 36, 49, 100, 400, 100, 100)
        if frame == 5:
            character.clip_draw(frame * 28 + 28,  190, 30, 49, 100, 400, 100, 100)
        if frame == 6:
            character.clip_draw(6 * 28 + 28,  190, 30, 49, 100, 400, 100, 100)
        frame = (frame + 1) % 7
        delay(0.1)


    update_canvas()
    handle_events()

close_canvas()