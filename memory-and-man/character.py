import pygame
from visuals import PlayerVisual, BeastVisual, CharacterVisual
from conventions import Point

class Character:
    def __init__(self, surface: pygame.Surface):
        self.name: str
        self.pos: Point = Point()
        self.velocity = {"target_point": Point(),
                         "speed": 0}
        self.visual = CharacterVisual(surface)
        self.max_speed = 10

    def move_towards(self, target_pos: Point):
        self.pos = self.pos.distance_to(target_pos.vec(), self.max_speed)

    def draw(self):
        self.visual.draw(center_pos=self.pos)


class Player(Character):
    def __init__(self, surface):
        super().__init__(surface)
        self.name = "player"
        self.visual = PlayerVisual(surface)
        self.max_speed = 30


class Beast(Character):
    def __init__(self, surface):
        super().__init__(surface)
        self.name = "beast"
        self.visual = BeastVisual(surface)
        self.max_speed = 20
