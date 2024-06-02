from pygame.time import get_ticks
from icecream import ic


class Timer:
    def __init__(self, duration, repeat=False, selfstart=False, func=None):
        self.Start_time = 0
        self.duration = duration
        self.repeat = repeat
        self.start_time = 0
        self.active = False
        self.func = func
        if selfstart:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    def deactivate(self):
        self. active = False
        self.Start_time = 0
        if self.repeat:
            self.activate()

    def update(self):
        if self. active:
            current_time = get_ticks()
            if current_time - self. start_time >= self.duration:
                if self.func: self.func()
                self. deactivate()

    def __exit__(self):
        for item in self.__dict__:
            ic(item)
            del item
        ic("=>EXIT!")
