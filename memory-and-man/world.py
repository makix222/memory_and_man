from typing import Union

import pygame
import simulation
from render import Renderer
from simulation import Simulation
from character import Player, Beast


class World:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.size = (self.width, self.height)
        self.screen = self.create_screen()
        self.physics = WorldPhysics()
        self.simulation = Simulation()
        self.renderer = Renderer(self.simulation.clock)
        self.characters = {}
        self.create_characters()

    def create_screen(self):
        return pygame.display.set_mode(self.size)

    def create_characters(self):
        self.characters = {"Player": Player(self.screen),
                           "Beast": Beast(self.screen)}
        for v in self.characters:
            self.renderer.add_objets_to_draw(v)

    def update(self):
        self.simulation.tick()

    def draw(self):
        self.renderer.draw_objects()



class WorldPhysics:
    def __init__(self):
        self.px_to_meter = 10

    def sim_calc(self):
        # Used later post init
        # Consumes sim and visual tick rates, size of screen
        # Sets object speeds and other values like friction
        pass
