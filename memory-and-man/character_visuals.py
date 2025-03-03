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

    def draw(self, center: Place, state):
        self.gen_rect(center)
        pygame.draw.rect(self.surface,
                         self.color,
                         self.rect)
        self.draw_velocity(center, state['velocity'], 20)
        self.draw_orientation(center, state['orientation'], 40)

    def draw_velocity(self,
                      place: Place,
                      velocity: pygame.Vector2,
                      scale: float = 1.0):
        if velocity.length() != 0:
            pygame.draw.line(surface=self.surface,
                             color=(255,40, 40),
                             start_pos=place.vec(),
                             end_pos=place.vec() + velocity * scale,
                             width=2)

    def draw_orientation(self,
                          place: Place,
                          orientation: pygame.Vector2,
                          size: float = 1.0):
        tip = (place.vec() + orientation * size)
        right = tip - (orientation.rotate(15)) * (size / 3)
        left = tip - (orientation.rotate(-15)) * (size / 3)
        points = [(tip.x, tip.y),
                  (right.x, right.y),
                  (left.x, left.y)]
        pygame.draw.polygon(surface=self.surface,
                            color=self.color,
                            points=points)
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
        self.drawn_sense_range = 0

    def draw_sense(self, sense_range):
        drawn_sense_ratio = (sense_range - self.drawn_sense_range) / sense_range
        sense_color = pygame.color.Color(*self.color,
                                         a=self.color.a * drawn_sense_ratio)
        pygame.draw.circle(self.surface,
                           sense_color,
                           self.rect.center,
                           self.drawn_sense_range,
                           width=int(1.0 + 3 * drawn_sense_ratio))
        if self.drawn_sense_range < sense_range:
            self.drawn_sense_range += 1
        else:
            self.drawn_sense_range = 0

