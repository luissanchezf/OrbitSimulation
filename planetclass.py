from pygame.examples.eventlist import virtual_x


class planet:
    def __init__(self, x, y, color, ratio, masa, e, a):
        self.x = x
        self.y = y
        self.e = e
        self.a = a
        self.vx = 0
        self.vy = 0
        self.color = color
        self.ratio = ratio
        self.masa = masa