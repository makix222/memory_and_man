import pygame
import enums

class Renderer:
    def __init__(self, sim_clock):
        self.render_mills = int(1000 / 60)
        render_event = pygame.event.Event(pygame.USEREVENT, {"type": enums.UserEvents})
        pygame.time.set_timer(render_event, self.render_mills)
        self.draw_objects = []

    def add_objets_to_draw(self, draw_object):
        if not hasattr(draw_object, "draw"):
            raise ValueError("provided object to draw does not have a draw function")
        self.draw_objects.append(draw_object)

    def handle_render_event(self):
        for each_obj in self.draw_objects:
            each_obj.draw()