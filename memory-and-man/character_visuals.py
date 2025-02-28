import pygame
from place import Place
from world import World


class CharacterVisual:
    def __init__(self, world: World):
        self.surface = world.screen
        self.color = pygame.Color(10, 10, 10)
        self.width = 20
        self.height = 20
        self.rect = None

    def gen_rect(self, center: Place):
        if self.rect is None:
            try:
                self.rect = pygame.Rect(center.x - self.width / 2,
                                        center.y - self.height / 2,
                                        self.width,
                                        self.height)
            except AttributeError as e:
                print(e)
                breakpoint()
        else:
            self.rect.center = center.pos()

    def draw(self, center: Place):
        self.gen_rect(center)
        pygame.draw.rect(self.surface,
                         self.color,
                         self.rect)

    def draw_velocity(self,
                      place: Place,
                      orientation: pygame.Vector2,
                      scale: float = 1.0):
        if orientation.length() != 0:
            pygame.draw.line(surface=self.surface,
                             color=self.color,
                             start_pos=place.vec(),
                             end_pos=place.vec() + orientation * scale,
                             width=2)
    # def draw_target(self,
    #                 place,
    #                 target):


class PlayerVisual(CharacterVisual):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = pygame.Color(10, 255, 10)


class BeastVisual(CharacterVisual):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = pygame.Color(165, 15, 15)
        self.height = 30
        self.width = 30
