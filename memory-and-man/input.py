import pygame
from simulation import World
from conventions import event_handler

class LocalInput:
    def __init__(self, world: World):
        self.mouse = Mouse(world)

    def update(self):
        self.mouse.update()

class Mouse:
    def __init__(self, world: World):
        self.world = world
        # pygame.mouse.set_visible(False)
        # pygame.mouse.set_pos(world.center.pos())

        self.vec = pygame.Vector2()
        self.pos = self._get_pos()
        self.buttons = []
        self.event_dict = {pygame.MOUSEBUTTONDOWN : self.button_down,
                           pygame.MOUSEBUTTONUP: self.button_up}

    def _get_pos(self):
        pos = pygame.mouse.get_pos()
        self.vec = pygame.Vector2(pos)
        self.pos = self.vec[:]
        return self.pos

    def set_pos(self, pos):
        self.vec = pygame.Vector2(pos)
        self.pos = self.vec[:]

    def update(self):
        event_handler(self.event_dict)
        pygame.draw.circle(surface=self.world.screen,
                           color=(154,65,123),
                           center=self.pos,
                           radius=40,
                           width=1)

    def button_down(self, event):
        self.set_pos(event.pos)
        self.buttons = event.button

    def button_up(self, event):
        pass



