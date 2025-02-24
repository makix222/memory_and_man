import pygame
import character_visuals
from conventions import Point

class Character:
    def __init__(self, surface: pygame.Surface):
        self.name: str
        self.pos: Point = Point()
        self.velocity = pygame.math.Vector2()
        self.visual = character_visuals.CharacterVisual(surface)
        self.max_speed = 1

    def move_towards(self, target_pos: Point):
        self.velocity = self.pos.move_to(target_pos.vec(), self.max_speed)

    def draw(self):
        self.visual.draw(center_pos=self.pos)


class Player(Character):
    def __init__(self, surface):
        super().__init__(surface)
        self.name = "player"
        self.visual = character_visuals.PlayerVisual(surface)
        self.max_speed = 3

    def draw(self):
        self.visual.draw(self.pos)
        self.visual.draw_velocity(self.pos.vec(),
                                  self.velocity,
                                  scale = 1)


class Beast(Character):
    def __init__(self, surface):
        super().__init__(surface)
        self.name = "beast"
        self.visual = character_visuals.BeastVisual(surface)
        self.max_speed = 2
