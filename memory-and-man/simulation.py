import pygame

class Simulation:
    def __init__(self):
        self.sim_tick_rate = 300
        self.clock = pygame.time.Clock()

    def tick(self):
        self.clock.tick(self.sim_tick_rate)