from typing import Union
import pygame
from conventions import Point


class CharacterVisual:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.color = pygame.Color(10, 10, 10)
        self.width = 20
        self.height = 20
        self.rect = None

    def gen_rect(self, center_pos: Point):
        midpoint = Point((
            int(self.width / 2),
            int(self.height / 2)
        ))
        if not self.rect:
            try:
                self.rect = pygame.Rect(
                    ((center_pos.x - midpoint.x),
                     (center_pos.y - midpoint.y)),
                    (self.width, self.height))
            except TypeError as e:
                print(e)
                breakpoint()
        else:
            self.rect.left = (center_pos.x - midpoint.x)
            self.rect.top = (center_pos.y - midpoint.y)

    def draw(self, center_pos: Point):
        self.gen_rect(center_pos)
        pygame.draw.rect(self.surface,
                         self.color,
                         self.rect)


class PlayerVisual(CharacterVisual):
    def __init__(self, surface):
        super().__init__(surface)
        self.color = pygame.Color(10, 255, 10)

    def draw_velocity(self,
                      center_pos: pygame.Vector2,
                      velocity: pygame.Vector2,
                      scale: float):
        pygame.draw.line(self.surface,
                         self.color,
                         center_pos,
                         velocity * scale)


class BeastVisual(CharacterVisual):
    def __init__(self, surface):
        super().__init__(surface)
        self.color = pygame.Color(165, 15, 15)
        self.height = 30
        self.width = 30
