import pygame
from conventions import Point

class Simulation:
    def __init__(self):
        self.sim_tick_rate = 300
        self.clock = pygame.time.Clock()

    def tick(self):
        self.clock.tick(self.sim_tick_rate)

class World:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        width = self.screen.get_width()
        height = self.screen.get_height()
        self.px_to_meter = 10
        self.sim_init()
        self.player_start_pos = Point((width * .4, height * .5))
        self.beast_start_pos = Point((width * .6, height * .5))

    def sim_init(self):
        # Used later post init
        # Consumes sim and visual tick rates, size of screen
        # Sets object speeds and other values like friction
        pass

    def draw(self):
        self.screen.fill((10, 10, 10))
