# BubbleScreenSaver0.0.2
import win32api
import win32con
import win32gui
from icecream import ic, install
install()
import random
import pygame_gui
from pymunk.pygame_util import to_pygame, DrawOptions
import pymunk
import IMG
# noinspection PyUnresolvedReferences
from Bubble_sprite import Bubble
from Debug import Debugger
from colors import *
from Ticker import Timer
import pygame as pg

"""

make window full screen, and transparent,*
auto launch bubbles
mouse body to pop bubbles -morning star?
bubbles that collide onto each other merge
option for parallax background
option for wallpaper background
render bubble img from blender

"""


def tostring(obj):
    if isinstance(obj, str):
        return '[!string %r with length %i!]' % (obj, len(obj))
    return repr(obj)


ic.configureOutput(includeContext=True, contextAbsPath=False,)
pymunk.pygame_util.positive_y_is_up = False


class BSS:
    def __init__(self):
        self.delta_time = None
        self.segment_shape = None
        self.start_button = None
        self.done = False
        self.ticks = 2500
        self.FPS = 60
        self.clock = pg.time.Clock()
        self._dt = self.clock.tick(self.FPS)
        self.S_WIDTH, self.S_HEIGHT = 800, 600
        self.screen_S = self.S_WIDTH, self.S_HEIGHT
        self.display = pg.display
        self.display.set_caption('Bubble Screen Saver')
        self.WRESurf = self.display.set_mode(self.screen_S, pg.RESIZABLE  , 0)
        self.hwnd = pg.display.get_wm_info()["window"]
        self.background = pg.Surface(size=self.screen_S)
        self.background.fill(color[aqua])
        self.draw_options = DrawOptions(self.WRESurf)
        self.draw_options.collision_point_color = color[black]
        self.space = pymunk.Space()
        self.ui_man = pygame_gui.UIManager(self.screen_S, theme_path='button_themes.json')
        # self.ui_man.set_visual_debug_mode(False)
        self.ImgLib = IMG.Lib()
        self.BubbleSprite_group = pg.sprite.Group()
        self.bubble_radius = 64
        self.bubble_diam = self.bubble_radius * 2
        self.PowerBubble = pg.transform.smoothscale(self.ImgLib.OGPowerBubble, (self.bubble_diam, self.bubble_diam))
        self.WinBox = []
        self.ui()
        self.Debug = False
        self.cycle_render = self.draw
        self.Number_of_bubbles = 0
        self.MAX_bubbles = 75
        self.DEBUG_OFF = pg.event.custom_type()
        self.Bug = Debugger(self.ui_man,self.DEBUG_OFF)
        self.Time_to_next_bubble = Timer(duration=350)

    def StartBubbles(self):
        if not self.Time_to_next_bubble.active:
            if self.Number_of_bubbles < self.MAX_bubbles:
                radius = random.randrange(20, 64)
                pos = self.S_WIDTH - radius, self.S_HEIGHT - radius
                self.Time_to_next_bubble = Timer(duration=350, func=self.spawn_bubble(self.PowerBubble, pos, radius))
                self.Time_to_next_bubble.activate()


    def create_segment(self, from_, to_, thickness, col):
        self.segment_shape = pymunk.Segment(self.space.static_body, from_, to_, thickness)
        self.segment_shape.color = color[col]
        self.segment_shape.elasticity = 0.03
        self.space.add(self.segment_shape)
        self.WinBox.append(self.segment_shape)

    def boxwindow(self):
        self.screen_S = self.WRESurf.get_size()
        self.WinBox.clear()
        self.S_WIDTH, self.S_HEIGHT = self.screen_S
        segment_thickness = 1
        a1, a2 = (0, 0), (0, self.S_WIDTH)  # left
        b1, b2 = (0, self.S_HEIGHT), (self.S_WIDTH, self.S_HEIGHT)  # bottom
        c1, c2 = (self.S_WIDTH, 0), (0, 0)  # top
        d1, d2 = (self.S_WIDTH, 0), (self.S_WIDTH, self.S_WIDTH)  # right
        self.create_segment(a1, a2, segment_thickness, red)
        self.create_segment(b1, b2, segment_thickness, wheat)
        self.create_segment(c1, c2, segment_thickness, white)
        self.create_segment(d1, d2, segment_thickness, green)

    def run(self):
        self.boxwindow()
        while not self.done:
            self.logic()
            self.event_handle()
            self.render()

    def event_handle(self):
        for event in pg.event.get():
            if event.type == pg.WINDOWMAXIMIZED:
                win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                                       win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
                win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*(0, 0, 0)), 127, win32con.ULW_ALPHA)
                pass # self.WRESurf = self.display.set_mode(self.WRESurf.get_size(),pg.NOFRAME,0, 1)
            if event.type == pg.WINDOWRESIZED:
                self.removebox()
                self.boxwindow()
                self.ui_man.set_window_resolution(self.screen_S)
                self.background = pg.Surface(size=self.screen_S)
                self.background.fill(color[grey20])
            # ic(self.screen_S)
            if event.type == pg.QUIT:
                self.done = True
                exit()
            # KeyEVENTS--------------------------------------------------------------
            # ic(self.pg_key[pg.K_BACKSLASH])
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                if event.key == pg.K_BACKSLASH:
                    if self.Debug is False:
                        self.Debug = not self.Debug
                        self.Bug = Debugger(self.ui_man,self.DEBUG_OFF)
                        self.Bug.draw_write(str(self.BubbleSprite_group), x=0, y=1)
                        self.Bug.draw_write(str(self.space.bodies), x=0, y=100)
                        self.cycle_render = self.draw_debug
                        ic.enable()
                    elif self.Debug is True:
                        self.Debug = not self.Debug
                        self.Bug.putaway()
                        ic.disable()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    pass
                if event.key == pg.K_BACKSLASH:
                    pass
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass  # ic(event.pos)
                if event.button == 3:
                    pass
            if event.type == self.DEBUG_OFF:
                self.to_draw()
            # UI EVENTS---------------------------------------------------------------------------------
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_button:
                    self.StartBubbles()

            self.ui_man.process_events(event)


    def logic(self):
        self.clock = pg.time.Clock()
        self._dt = self.clock.tick(self.FPS)
        self.delta_time = self.FPS / 1000
        self.ui_man.update(self.delta_time)
        self.space.step(self.delta_time)
        self.StartBubbles() 
        self.Time_to_next_bubble.update()
        self.BubbleSprite_group.update()

    def render(self):
        self.WRESurf.blit(self.background, (0, 0))
        self.cycle_render()
        self.ui_man.draw_ui(self.WRESurf)
        self.display.flip()

    # noinspection PyUnusedLocal
    def spawn_bubble(self, img, pos, radius):
        new_bubble = (f'bub{self.Number_of_bubbles} = Bubble(self.WRESurf, self.space)\n'
                      f'bub{self.Number_of_bubbles}.sp(pos, radius, img)')
        exec(new_bubble)
        to_group = f'self.BubbleSprite_group.add(bub{self.Number_of_bubbles}.Sprite)'
        exec(to_group)
        self.Number_of_bubbles += 1
        ic(self.Number_of_bubbles)

    def draw(self):
        self.BubbleSprite_group.draw(self.WRESurf)

    def draw_debug(self):
        self.space.debug_draw(self.draw_options)
        self.BubbleSprite_group.draw(self.WRESurf)
        # self.ui_man.set_visual_debug_mode(True)

    def removebox(self):
        for Seg in self.WinBox:
            self.space.remove(Seg)

    def ui(self):
        br_rect = pg.Rect((0, 0,), (100, 30))
        br_rect.bottomright = (0, 0)
        self.start_button = pygame_gui.elements.UIButton(br_rect,
                                                         'Start Bubbles', self.ui_man,
                                                         self.ui_man.root_container,
                                                         anchors={'right': 'right', 'bottom': 'bottom'})

    def to_draw(self):
        self.cycle_render = self.draw



# RUN---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    pg.init()
    BSS().run()
    pg.quit()
