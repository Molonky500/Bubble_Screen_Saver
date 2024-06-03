import math
import pymunk
from Ticker import Timer
from icecream import ic
from colors import *
from decimal import *
getcontext().prec = 6

import pygame as pg

# noinspection PyProtectedMember
from pymunk.pygame_util import to_pygame, Vec2d


class BubbleColl:
    def __init__(self, screen, space):
        super().__init__()
        self.shape = None
        self.pos = None
        self.radius = None
        self.screen = screen
        self.space = space
        self.body = None

    def prep(self, pos, radius, ):
        self.radius = radius
        self.body = pymunk.Body(1, 100)
        self.body.position = pos
        self.pos = to_pygame(Vec2d(*self.body.position).int_tuple, self.screen)
        self.shape = pymunk.Circle(body=self.body, radius=self.radius, )
        self.shape.elasticity = 1
        self.shape.friction = 10
        self.shape.color = color[orange]

    def place(self):
        self.space.add(self.body, self.shape)
        self.body.apply_impulse_at_local_point((-100, -100), (0, 0))


class BubbleSprite(pg.sprite.Sprite):
    def __init__(self, screen, space):
        # Constructor. Pass in the color of the block,
        # and its x and y position
        super().__init__()
        self.rect = None
        self.image = None
        self.original_image = None
        self.size = None
        self.coll = None
        self.ad = None
        self.screen = screen
        self.space = space
        self.s_width, self.s_height = self.screen.get_size()

    def paint(self, image, size, coll, auto_destroy):
        self.ad = auto_destroy
        self.coll = coll
        self.original_image = image
        self.size = size * 2
        self.original_image = pg.transform.smoothscale(self.original_image, (self.size, self.size))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.coll.body.position)
        self.color_time = Timer(2250, repeat=True, start=True,
                                func=self.colorize_array)

    def size_of_screen(self):
        self.s_width, self.s_height = self.screen.get_size()

    def update(self):
        self.color_time.update()
        self.rect.center = self.coll.body.position
        self.image = pg.transform.rotate(self.original_image, math.degrees(-self.coll.body.angle))
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.coll.body.position[0] >= self.s_width + self.size or self.coll.body.position[0] <= 0 - self.size:
            ic('out of bounds:', self.coll.body.position)
            self.end()
        elif self.coll.body.position[1] >= self.s_height + self.size or self.coll.body.position[1] <= 0 - self.size:
            ic('out of bounds:', self.coll.body.position)
            self.end()

    def colorize_array(self):
        pix_ar = pg.PixelArray(self.original_image)
        w, h = pix_ar.shape
        r, g, b, _ = color[cycle()]
        for x in range(w):
            for y in range(h):
                a = self.original_image.get_at((x, y))[3]
                pix_ar[x, y] = pg.Color(r, g, b, a)
        pix_ar.close()
        del pix_ar


    def end(self):
        self.kill()
        self.ad()


class Bubble:
    def __init__(self, screen, space):
        self.radius = None
        self.pos = None
        self.coll = BubbleColl(screen, space)
        self.Sprite = BubbleSprite(screen, space)
        self.space = space

    def sp(self, pos, radius, img):
        self.pos = pos
        self.radius = radius
        self.coll.prep(self.pos, self.radius, )
        self.coll.place()
        self.Sprite.paint(img, radius, self.coll, self.remove)

    def remove(self):
        self.space.remove(self.coll.shape, self.coll.body)
        ic(self.coll, "removed")
        self.__exit__()

    def __exit__(self):
        ic(self.__dict__)
        for item in self.__dict__:
            ic(item)
            del item
        ic("=>EXIT!")
