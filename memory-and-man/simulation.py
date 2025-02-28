import pygame

class Simulation:
    def __init__(self):
        self.sim_tick_rate = 300
        self.clock = pygame.time.Clock()
        self.paused = False
        self.update_list = []

    def add_objects_to_update(self, update_object):
        if not hasattr(update_object, "update"):
            raise ValueError(f"provided object {update_object} does not have a draw function")
        self.update_list.append(update_object)

    def tick(self):
        self.clock.tick(self.sim_tick_rate)
        if not self.paused:
            for each_entity in self.update_list:
                each_entity.update()

    def pause(self):
        self.paused = True


    def unpause(self):
        self.paused = False
