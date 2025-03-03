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
        self.walk_speed = 1
        self.run_speed = 1.25
        self.full_rotation_time_s = .5
        self.deg_per_tick = (360 / self.full_rotation_time_s) / self.world.tick_per_sec
        self.friction = .4
        self.state = {"moving": False,
                      "speed": 0.0,
                      "velocity": pygame.Vector2(),
                      "orientation": pygame.Vector2(),
                      "focus": Place()}

    def _post_init(self):
        self.place: Place = self.world.starting_places[self.name]
        self.state['focus_place'] = self.world.center
        self.state['orientation']: pygame.Vector2 = self.place.point_to(self.state['focus_place'].vec()).normalize()

    def update(self):
        self.apply_friction()
        self.move()
        self.rotate_orientation()

    def apply_friction(self):
        self.state['velocity'] += -self.state['velocity'] * self.friction
        if self.state['velocity'].magnitude() < .1:
            self.state['velocity'] = pygame.Vector2()

    def rotate_orientation(self, simple=True):
        """Two ways: Simple, and complex. Simple is snap to point, complex is rotate to point"""
        if simple:
            self.state['orientation'] = self.place.point_to(self.state['focus_place'].vec())
        else:
            theta = self.state['orientation'].angle_to(self.state['focus_place'].vec())
            if theta < self.deg_per_tick:
                self.state['orientation'] = self.place.point_to(self.state['focus_place'].vec())
            else:
                norm_slerp_value = self.deg_per_tick / theta
                # print(f"theta: {theta}"
                #       f"self.state['orientation'], {self.state['orientation']}"
                #       f"self.state['focus_place'], {self.state['focus_place']}")
                self.state['orientation'].slerp(self.state['focus_place'].vec(), norm_slerp_value)

    def move(self):
        self.place.move_place(velocity=self.state['velocity'])

    def draw(self):
        self.visual.draw(self.place, self.state)


class Player(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "player"
        self.visual = character_visuals.PlayerVisual(args[0])
        self.walk_speed = 1.2
        self.run_speed = 3
        self._post_init()

    def update(self):
        commands = self.local_input.get_commands()
        if commands:
            self.state['speed'] = 0
            if "walk" in commands or "forward" in commands:
                self.state['speed'] = self.walk_speed
                if "run" in commands:
                    self.state['speed'] = self.run_speed
            if "back" in commands:
                self.state['speed'] = -self.walk_speed
                if "run" in commands:
                    self.state['speed'] = -self.run_speed
            self.state['velocity'] += self.state['orientation'] * self.state['speed']
            if "left" in commands:
                self.state['velocity'] += self.state['orientation'].rotate(-90)
            if "right" in commands:
                self.state['velocity'] += self.state['orientation'].rotate(90)

        self.state['focus_place'] = Place(pos=self.local_input.mouse_pos)
        super().update()

    def draw(self):
        super().draw()
        # self.visual.draw_velocity(self.place,
        #                           self.state['velocity'],
        #                           scale=30)

    def move(self):
        super().move()
        self.event_handler.add_event(producer=EventUser.player,
                                     consumer=EventUser.beast,
                                     data={"place": self.place,
                                           "orientation": self.state['orientation'],
                                           "speed": self.state['speed']})


class Beast(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "beast"
        self.visual = character_visuals.BeastVisual(args[0])
        self.state['speed'] = 0
        self.walk_speed = 2
        self.sense_radius = 100
        self._post_init()

    def update(self):
        player_data = self.event_handler.get_event_data(producer=EventUser.player, consumer=EventUser.beast)
        if len(player_data) > 0:
            self.state['focus_place'] = player_data[-1]['place']
            distance_to_player = self.place.point_to(self.state['focus_place'].vec(), normalized=False).magnitude()
            if distance_to_player < self.sense_radius:
                self.state['speed'] = self.walk_speed
                self.state['velocity'] = self.state['orientation'] * self.state['speed']
        super().update()

    def draw(self):
        super().draw()
        # self.visual.draw_velocity(self.place, self.state['velocity'], 30)
        self.visual.draw_sense(self.sense_radius)
