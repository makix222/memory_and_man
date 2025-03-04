import pygame
import random
import itertools
from typing import Dict
from place import Place
from simulation import Simulation


class World:
    def __init__(self, screen: pygame.Surface, sim: Simulation):
        self.screen = screen
        self.sim = sim
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.center = Place(pos=(self.width * .5, self.height * .5))
        self.px_per_meter = 10
        self.sim_init()
        self.starting_places: Dict[str: Place] = {"player": Place(pos=(self.width * .8,
                                                                      self.height * .8)),
                                                  "beast": Place(pos=(self.width * .3,
                                                                      self.height * .3))
                                                  }
        self.window_focused = False

        self.background_color = (0, 0, 0)
        self.debug_color = [0, 0, 0]
        self.counter = 1
        self.direction = 1
        self.step = 5
        self.loop = 0

        self.tick_per_sec = self.sim.sim_tick_rate

    def sim_init(self):
        # Used later post init
        # Consumes sim and visual tick rates, size of screen
        # Sets object speeds and other values like friction
        pass

    def update(self):
        # as the world grows, items will need to change.
        # place changes here.
        pass

    def draw(self):
        self.screen.fill(self.background_color)
        self._debug_active_render()

    def _debug_active_render(self):
        padding = 4
        pygame.draw.rect(self.screen,
                         self.debug_color,
                         pygame.Rect((padding,
                                      padding),
                                     (self.width - 2*padding,
                                      self.height - 2*padding)),
                         width=2,
                         border_radius=2)

        permutations = list(itertools.product([self.counter, 0], repeat=3))[1:]
        self.debug_color = permutations[self.loop % len(permutations)]
        self.counter += self.step if self.direction else -self.step

        if self.counter >= 255:
            self.counter = 255
            self.direction = 0
        elif self.counter <= 0:
            self.counter = 0
            self.loop = random.randint(0, len(permutations) - 2)
            self.direction = 1
