from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        self.image.draw(screen_x, screen_y )

        # draw_rectangle(*self.get_bb())

    def update(self):

        pass

    def get_bb(self):
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        return screen_x - 10, screen_y - 10, screen_x + 10, screen_y + 10

    def handle_collision(self, group, other):
        # print("collision!!")
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass

