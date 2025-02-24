import pygame


class Point:
    def __init__(self, pos=(None, None)):
        self.x: int = pos[0]
        self.y: int = pos[1]
        if self.x is not None and self.y is not None:
            self.x = int(self.x)
            self.y = int(self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def vec(self):
        return pygame.Vector2(self.x, self.y)

    def move_to(self,
                 target: pygame.Vector2,
                 clamp = None):
        if clamp:
            try:
                new_vec = self.vec() + (target - self.vec()).clamp_magnitude(clamp)
            except ValueError:
                return self.vec()
        else:
            new_vec = self.vec() + (target - self.vec())
        self.x = new_vec.x
        self.y = new_vec.y
        return new_vec
