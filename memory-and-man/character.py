import pygame
import character_visuals
from place import Place
from world import World
from input import LocalInput
from events import EventUser, EventHandler


class Character:
    def __init__(self,
                 world: World,
                 local_input: LocalInput,
                 event_handler: EventHandler):
        """Parameters shared between all characters in world"""
        self.world = world
        self.local_input = local_input
        self.event_handler = event_handler
        self.visual = character_visuals.CharacterVisual(world)
        self.name: str = ""
        self.place: Place = Place()
        self.orientation_target: Place = Place()
        self.orientation: pygame.Vector2 = pygame.Vector2()
        self.speed = 0
        self.walk_speed = 1
        self.run_speed = 1.25
        self.full_rotation_time_s = .5
        self.deg_per_tick = (360 / self.full_rotation_time_s) / self.world.tick_per_sec

    def _post_init(self):
        self.place: Place = self.world.starting_places[self.name]
        self.orientation_target: Place = Place(pos=(self.world.center.x,
                                                    0))
        self.orientation: pygame.Vector2 = self.place.point_to(self.orientation_target).normalize()

    def update(self):
        self.rotate_orientation()
        if self.speed > 0:
            self.move()

    def rotate_orientation(self, simple=True):
        """Two ways: Simple, and complex. Simple is snap to point, complex is rotate to point"""
        if simple:
            self.orientation = self.place.point_to(self.orientation_target)
        else:
            theta = self.orientation.angle_to(self.orientation_target.vec())
            if theta < self.deg_per_tick:
                self.orientation = self.place.point_to(self.orientation_target)
            else:
                norm_slerp_value = self.deg_per_tick / theta
                # print(f"theta: {theta}"
                #       f"self.orientation, {self.orientation}"
                #       f"self.orientation_target, {self.orientation_target}")
                self.orientation.slerp(self.orientation_target.vec(), norm_slerp_value)


    def move(self):
        self.place.move_place(self.orientation)

    def draw(self):
        self.visual.draw(self.place)


class Player(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "player"
        self.visual = character_visuals.PlayerVisual(args[0])
        self.speed = 0
        self.walk_speed = 5
        self._post_init()

    def update(self):
        commands = self.local_input.get_commands()
        if "run" in commands:
            self.speed += self.run_speed
        elif "walk" in commands:
            self.speed += self.walk_speed
        else:
            self.speed = 0

        self.orientation_target = Place(pos=self.local_input.mouse_pos)
        super().update()

    def draw(self):
        super().draw()
        self.visual.draw_velocity(self.place,
                                  self.orientation,
                                  scale = 30)

    def move(self):
        super().move()
        self.event_handler.add_event(producer=EventUser.player,
                                     consumer=EventUser.beast,
                  data={"place": self.place,
                        "orientation": self.orientation,
                        "speed": self.speed})


class Beast(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "beast"
        self.visual = character_visuals.BeastVisual(args[0])
        self.speed = 0
        self.walk_speed = 2
        self._post_init()

    def update(self):
        player_data = self.event_handler.get_event_data(consumer=EventUser.beast, producer=EventUser.player)
        self.speed = 0
        if len(player_data) > 0:
            self.orientation_target = player_data[-1]['place']
            distance_to_player = self.place.point_to(self.orientation_target).magnitude()
            print(f"Beast speed before update: {self.speed}"
                  f"distance: {distance_to_player}")
            if distance_to_player < 10:
                self.speed = self.walk_speed
            else:
                self.speed = 0
            print(f"beast start speed: {self.speed}")
        super().update()
        print(f"beast end speed: {self.speed}")

