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

    def point_to(self,
                 target: pygame.Vector2,
                 normalized=True) -> pygame.Vector2:
        diff = target - self.vec()
        if normalized:
            diff = diff.normalize()
        return diff

    def move_place(self,
                   orientation: pygame.Vector2=None,
                   speed=None,
                   velocity: pygame.Vector2=None):
        if velocity is None:
            if not orientation or not speed:
                raise ValueError("Cant move without either a velocity, or an orientation and speed")
            velocity = orientation * speed
            new_pos = self.vec() + velocity
            self.x = new_pos.x
            self.y = new_pos.y
            return
        temp_vec = self.vec() + velocity
        self.x = temp_vec.x
        self.y = temp_vec.y

