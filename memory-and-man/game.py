import pygame

from events import EventUser, EventHandler
from input import LocalInput
from simulation import Simulation
from world import World
from render import Renderer
from character import Player, Beast


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.size = (self.width, self.height)
        self.screen = self.create_screen()
        self.event_handler = EventHandler()
        self.sim = Simulation()
        self.world = World(self.screen, self.sim)
        self.sim.add_objects_to_update(self.world)
        self.renderer = Renderer(self.world, self.event_handler)
        self.local_input = LocalInput(self.world, self.event_handler)
        self.renderer.add_objets_to_draw(self.local_input)
        self.sim.add_objects_to_update(self.local_input)
        self.characters = {}
        self.create_characters()
        for v in self.characters.values():
            self.renderer.add_objets_to_draw(v)
            self.sim.add_objects_to_update(v)

        self.event_map = {pygame.WINDOWFOCUSGAINED: self.window_focused,
                           pygame.WINDOWFOCUSLOST: self.window_unfocused}


    def create_screen(self):
        return pygame.display.set_mode(self.size)

    def create_characters(self):
        self.characters = {"Player": Player(self.world,
                                            self.local_input,
                                            self.event_handler),
                           "Beast": Beast(self.world,
                                          self.local_input,
                                          self.event_handler)}

    def update(self):
        """Required to run once a game loop"""
        self.sim.tick()
        self.event_handler.handle_events(self.event_map)
        self.user_events()

    def user_events(self):
        if len(self.event_handler.get_event_data(producer=EventUser.render, consumer=EventUser.game)) > 0:
            self.renderer.render_update()

    def window_focused(self, event):
        # pygame.event.set_grab(True)
        # pygame.mouse.set_visible(False)
        # pygame.mouse.set_pos(self.world.center.pos())
        # self.world.debug_color = (255,12,12)
        self.world.window_focused = True
        self.sim.unpause()

    def window_unfocused(self, event):
        # pygame.event.set_grab(False)
        # pygame.mouse.set_visible(True)
        # self.world.debug_color = (12,12,255)
        self.world.window_focused = False
        self.sim.pause()




