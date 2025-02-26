import pygame
import character_visuals
from conventions import Place
from simulation import World
from input import LocalInput

class Character:
    def __init__(self, world: World, local_input: LocalInput):
        """Parameters shared between all characters in world"""
        self.world = world
        self.local_input = local_input
        self.name: str = ""
        self.place = None
        self.velocity = pygame.math.Vector2()
        self.visual = character_visuals.CharacterVisual(world)
        self.max_speed = 1

    def update(self):
        self.set_velocity(self.local_input.mouse.place)
        self.update_pos()

    def set_velocity(self, target: Place):
        diff_vec = target.diff(self.place)
        if diff_vec.length() < .1:
            return
        self.velocity = diff_vec.clamp_magnitude(self.max_speed)

    def update_pos(self):
        self.place.update(self.velocity)

    def draw(self):
        self.visual.draw(self.place)


class Player(Character):
    def __init__(self, world, local_input):
        super().__init__(world, local_input)
        self.name = "player"
        self.visual = character_visuals.PlayerVisual(world)
        self.max_speed = 3
        self.place = self.world.starting_places[self.name]

    def draw(self):
        self.visual.draw(self.place)
        self.visual.draw_velocity(self.place.vec(),
                                  self.velocity,
                                  scale = 1)


class Beast(Character):
    def __init__(self, world, local_input):
        super().__init__(world, local_input)
        self.name = "beast"
        self.visual = character_visuals.BeastVisual(world)
        self.max_speed = 2
        self.place = self.world.starting_places[self.name]

