# File for debugging
import pygame_gui
from pygame_gui.elements import UITextBox
from pygame_gui.elements.ui_window import UIWindow
import pygame as pg
from icecream import ic

ic.configureOutput(includeContext=False, contextAbsPath=False)


class TxtBox(UITextBox):
    def __init__(self, text, man, parent, text_rect):
        self.text = text.removeprefix('<').removesuffix('>', )
        self.man = man
        self.parent = parent
        self.text_rect = text_rect
        super().__init__(html_text=self.text, relative_rect=self.text_rect,
                         manager=self.man,
                         container=self.parent,
                         parent_element=self.parent,
                         anchors={'left': 'left', 'top': 'top'})

    def draw_write(self, text):
        """
        write to debug boxes
        :type text: str
        """
        self.text = text
        infotext = self.text.removeprefix('<').removesuffix('>', )
        self.text = f'Debug:{infotext}'
        self.text_rect.topleft = (0, 0)
        self.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,
                               params={'time_per_letter': 0.0001,
                                       'time_per_letter_deviation': 0.0003}
                               )
        self.enable()

    def __exit__(self):
        ic(self.__dict__)
        for _ in self.__dict__:
            del _
            ic("=>EXIT!")

    def end(self):
        self.__exit__()
        self.kill()


class Debugger(UIWindow):
    def __init__(self, man, event):
        self.text = None
        self.debug_rect = pg.Rect((0, 0), (320, 320))
        self.ui_man = man
        self.ui_man.get_theme().load_theme('Debug_theme.json')
        self.event = event
        super().__init__(self.debug_rect, self.ui_man,
                         window_display_title='Debug',
                         object_id='#Debug_window',
                         )
        self.resizable = True
        self.display_surf = pg.display.get_surface()
        self.display_surf_size = self.display_surf.get_size()
        self.on_close_window_button_pressed = self.putaway
        self.rect_list = []
        self.count = 0
        self.hide()

    def draw_write(self, info, x=0, y=0, ):
        self.text = info
        w = self.relative_rect.w
        h = self.relative_rect.h / (2 + self.count)
        newbox = f'self.debug_text{self.count} =  TxtBox(self.text,self.ui_man,self,pg.Rect(({x, y}), (w, h)))'
        writebox = f'self.debug_text{self.count}.draw_write(self.text)'
        exec(newbox)
        exec(writebox)
        add_to_list = f'self.rect_list.append(self.debug_text{self.count})'
        self.count += 1
        self.show()

    def putaway(self):
        for box in self.rect_list:
            ic(box)
            box.end()
        self.kill()
        ic(pg.event.post(pg.event.Event(self.event)))
        self.__exit__()

    def __exit__(self):
        for item in self.__dict__:
            ic(item)
            del item
        ic("=>EXIT!")
