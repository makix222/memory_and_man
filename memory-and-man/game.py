from typing import Union

import pygame
from simulation import Simulation, World
from render import Renderer
from character import Player, Beast


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.size = (self.width, self.height)
        self.screen = self.create_screen()
        self.simulation = Simulation()
        self.world = World(self.screen)
        self.renderer = Renderer(self.world)
        self.characters = {}
        self.create_characters()

    def create_screen(self):
        return pygame.display.set_mode(self.size)

    def create_characters(self):
        self.characters = {"Player": Player(self.world),
                           "Beast": Beast(self.world)}
        for v in self.characters.values():
            self.renderer.add_objets_to_draw(v)

    def update(self):
        """Required to run once a game loop"""
        self.simulation.tick()

    def render_update(self):
        """Call from event handler to perform visual updates"""
        self.renderer.render_update()




