import pygame
from conventions import Place
from simulation import World


class CharacterVisual:
    def __init__(self, world: World):
        self.surface = world.screen
        self.color = pygame.Color(10, 10, 10)
        self.width = 20
        self.height = 20
        self.rect = None

    def gen_rect(self, center: Place):
        midpoint = Place((
            int(self.width / 2),
            int(self.height / 2)
        ))
        if not self.rect:
            try:
                self.rect = pygame.Rect(
                    ((center.x - midpoint.x),
                     (center.y - midpoint.y)),
                    (self.width, self.height))
            except AttributeError as e:
                print(e)
                breakpoint()
        else:
            self.rect.left = (center.x - midpoint.x)
            self.rect.top = (center.y - midpoint.y)

    def draw(self, center: Place):
        self.gen_rect(center)
        pygame.draw.rect(self.surface,
                         self.color,
                         self.rect)


class PlayerVisual(CharacterVisual):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = pygame.Color(10, 255, 10)

    def draw_velocity(self,
                      place: pygame.Vector2,
                      velocity: pygame.Vector2,
                      scale: float):
        if velocity.length() != 0:
            pygame.draw.line(surface=self.surface,
                             color=self.color,
                             start_pos=place,
                             end_pos=velocity.normalize() * scale)


class BeastVisual(CharacterVisual):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = pygame.Color(165, 15, 15)
        self.height = 30
        self.width = 30
