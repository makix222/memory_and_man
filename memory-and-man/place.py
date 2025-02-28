import pygame

class Place:
    def __init__(self,
                 place=None,
                 pos=(None, None),
                 vec: pygame.Vector2=None):
        self.x = pos[0]
        self.y = pos[1]
        if place and str(type(place)) == "Place":
            self.x = place.x
            self.y = place.y
        if vec:
            self.x = vec.x
            self.y = vec.y
        if self.x is not None and self.y is not None:
            self.x = int(self.x)
            self.y = int(self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def vec(self):
        return pygame.Vector2(self.x, self.y)

    def pos(self):
        return self.x, self.y

    def point_to(self, target) -> pygame.Vector2:
        return (target.vec() - self.vec()).normalize()

    def move_place(self, velocity: pygame.Vector2):
        if velocity.magnitude() == 0:
            return
        new_pos = self.vec() + velocity
        self.x = new_pos.x
        self.y = new_pos.y
