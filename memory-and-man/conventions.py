import pygame


class Point:
    def __init__(self, pos=(None, None)):
        self.x: int = pos[1]
        self.y: int = pos[0]
        if self.x is not None and self.y is not None:
            self.x = int(self.x)
            self.y = int(self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def vec(self):
        return pygame.Vector2(self.x, self.y)

    def distance_to(self,
                 target: pygame.Vector2,
                 clamp = None):
        if clamp:
            return (self.vec() - target).clamp_magnitude(clamp)
        return (self.vec() - target).magnitude()

