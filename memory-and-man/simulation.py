import pygame
from conventions import Place

class Simulation:
    def __init__(self):
        self.sim_tick_rate = 300
        self.clock = pygame.time.Clock()
        self.paused = False

    def tick(self):
        self.clock.tick(self.sim_tick_rate)

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

class World:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.middle = Place((self.width * .5, self.height * .5))
        self.px_to_meter = 10
        self.sim_init()
        self.starting_places = {"player": self.middle,
                                "beast": Place((self.width * .3,
                                                self.height * .3))}
        self.debug_color = (10, 10, 10)


    def sim_init(self):
        # Used later post init
        # Consumes sim and visual tick rates, size of screen
        # Sets object speeds and other values like friction
        pass

    def draw(self):
        self.screen.fill((10, 10, 10))
        pygame.draw.circle(self.screen,
                           color=self.debug_color,
                           center=self.middle.pos(),
                           radius=40,
                           width=2)
