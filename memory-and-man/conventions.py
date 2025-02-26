from typing import Type

import pygame


class Place:
    def __init__(self, pos=(None, None)):
        self.x: int = pos[0]
        self.y: int = pos[1]
        if self.x is not None and self.y is not None:
            self.x = int(self.x)
            self.y = int(self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def vec(self):
        return pygame.Vector2(self.x, self.y)

    def pos(self):
        return self.x, self.y

    def diff(self, target) -> pygame.Vector2:
        return target.vec() - self.vec()

    def update(self, velocity: pygame.Vector2):
        new_pos = self.vec() + velocity
        self.x = new_pos.x
        self.y = new_pos.y


def event_handler(event_dict: dict):
    for event in pygame.event.get(list(event_dict.keys()), pump=False):
        event_func = event_dict.get(event.type)
        if event_func:
            event_func(event=event)
