import pygame
from enums import UserEvents
from simulation import World

class Renderer:
    def __init__(self, world: World):
        """Sets up the render pipeline. Sets fps, sets render event timer."""
        self.render_mills = int(1000 / 60)
        render_event = pygame.event.Event(pygame.USEREVENT,
                                          {"name": UserEvents.RENDER})
        pygame.time.set_timer(render_event, self.render_mills)
        self.objects_to_draw = [world] # Must draw the world first.

    def add_objets_to_draw(self, draw_object):
        if not hasattr(draw_object, "draw"):
            raise ValueError(f"provided object {draw_object} does not have a draw function")
        self.objects_to_draw.append(draw_object)

    def render_update(self):
        for each_obj in self.objects_to_draw:
            each_obj.draw()