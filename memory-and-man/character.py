import pygame
import character_visuals
from conventions import Point
from simulation import World

class Character:
    def __init__(self, world: World):
        """Parameters shared between all characters in world"""
        self.world = world
        self.name: str
        self.pos: Point = Point()
        self.velocity = pygame.math.Vector2()
        self.visual = character_visuals.CharacterVisual(world)
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
        self.pos = self.world.player_start_pos

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
        self.pos = self.world.beast_start_pos
