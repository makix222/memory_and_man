import pygame
from world import World
from events import EventHandler

class LocalInput:
    def __init__(self, world: World, event_handler: EventHandler):
        self.mouse = Mouse(world, event_handler)
        self.keyboard = Keyboard(world, event_handler)
        self.command_map = {"mouse": {1: "walk"},
                            "keyboard": {"k_lshift": "run"}}
        self.commands = {"walk": 0,
                         "run": 0}
        self.mouse_pos = (0,0)

    def update(self):
        self.mouse.update()
        self.keyboard.update()
        self.check_inputs_for_commands()

    def check_inputs_for_commands(self):
        for k, v in self.command_map["mouse"].items():
            self.commands[v] = self.mouse.state.get(k, 0)
        for k, v in self.command_map["keyboard"].items():
            self.commands[v] = self.keyboard.keys.get(k, 0)
        self.mouse_pos = self.mouse.state['pos']

    def draw(self):
        self.mouse.draw()
        self.keyboard.draw()

    def get_commands(self):
        return [k for k, v in self.commands.items() if v != 0]


class Mouse:
    def __init__(self, world: World, event_handler: EventHandler):
        self.world = world
        self.event_handler = event_handler
        self.state = {1: 0,
                      2: 0,
                      3: 0,
                      "pos": self.world.center.pos()}
        self.event_map = {pygame.MOUSEBUTTONDOWN : self._button_down,
                           pygame.MOUSEBUTTONUP: self._button_up,
                           pygame.MOUSEMOTION: self._motion}
        self.btn_duration = 0
        self._max_radius = 30

    def update(self):
        self.event_handler.handle_events(self.event_map)

    def draw(self):
        if self.btn_duration > 1:
            pygame.draw.circle(surface=self.world.screen,
                               color=(154,65,123),
                               center=self.state['pos'],
                               radius=self.btn_duration,
                               width=1)

    def _button_down(self, event):
        # print(event, self.buttons)
        self.state[event.button] = 1
        self.btn_duration += .1 * (self._max_radius - self.btn_duration)

    def _button_up(self, event):
        # print(event, self.buttons)
        self.state[event.button] = 0
        self.btn_duration = 0

    def _motion(self, event):
        self.state["pos"] = event.pos


class Keyboard:
    def __init__(self, world: World, event_handler: EventHandler):
        self.world = world
        self.event_handler = event_handler
        self.keys = {}
        self.event_map = {pygame.KEYDOWN: self._keydown,
                           pygame.KEYUP: self._keyup}

    def update(self):
        self.event_handler.handle_events(self.event_map)

    def draw(self):
        pass

    def _keydown(self, event):
        self.keys[event.key] = 1

    def _keyup(self, event):
        self.keys[event.key] = 0





