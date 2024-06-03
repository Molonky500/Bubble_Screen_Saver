from pygame.time import get_ticks
from icecream import ic


class Timer:
    def __init__(self, duration, repeat=False, start=False, func=None):
        self.duration = duration
        self.repeat = repeat
        self.active = False
        self.func = func
        if start:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()
        else:
            self.__exit__()
            ic.enable()

    def update(self):
        if self.active:
            current_time = get_ticks()
            if current_time - self.start_time >= self.duration:
                if self.func:
                    self.func()
                self.deactivate()

    def __exit__(self):
        for item in self.__dict__:
            ic(item)
            del item
        ic("=>EXIT!")
        ic.disable()
