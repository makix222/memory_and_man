import pygame

from enums import UserEvents
from input import LocalInput
from simulation import Simulation, World
from render import Renderer
from character import Player, Beast
from conventions import event_handler


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.size = (self.width, self.height)
        self.screen = self.create_screen()
        self.sim = Simulation()
        self.world = World(self.screen)
        self.renderer = Renderer(self.world)
        self.local_input = LocalInput(self.world)
        self.characters = {}
        self.create_characters()

        self.event_dict = {pygame.WINDOWFOCUSGAINED: self.window_focused,
                           pygame.WINDOWFOCUSLOST: self.window_unfocused,
                           pygame.USEREVENT: self.user_events}

    def create_screen(self):
        return pygame.display.set_mode(self.size)

    def create_characters(self):
        self.characters = {"Player": Player(self.world, self.local_input),
                           "Beast": Beast(self.world, self.local_input)}
        for v in self.characters.values():
            self.renderer.add_objets_to_draw(v)

    def update(self):
        """Required to run once a game loop"""
        self.sim.tick()
        self.local_input.update()
        event_handler(self.event_dict)

    def user_events(self, event):
        if event.dict['name'] == UserEvents.RENDER:
            self.render_update()

    def render_update(self):
        """Call from event handler to perform visual updates"""
        self.renderer.render_update()

    def window_focused(self, event):
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self.world.debug_color = (255,12,12)
        self.sim.pause()

    def window_unfocused(self, event):
        pygame.event.set_grab(False)
        pygame.mouse.set_visible(True)
        self.world.debug_color = (12,12,255)
        self.sim.unpause()




