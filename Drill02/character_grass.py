from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


while(1):
    x = 400
    y = 90
    while(x < 750):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)
    
    while(y < 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750,y)
        y = y + 2
        delay(0.01)

    while(x > 50):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.01)
    
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.01)
    
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)
        
    degree = 1
    for degree in range (1, 270):
        clear_canvas_now()
        grass.draw_now(400, 30)
        radian = (degree * math.pi / 100) 
        character.draw_now(400 + math.sin(radian) * 100 , 300 + math.cos(radian) * 100)
        delay(0.01)
            

    
close_canvas()
