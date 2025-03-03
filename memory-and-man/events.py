import pygame
from enum import Enum

class EventUser(Enum):
    any = 0
    render = 1
    game = 2
    player = 3
    beast = 4


class EventHandler:
    def __init__(self):
        self.event_counts = 0
        self.custom_event_types = {}

    @staticmethod
    def handle_events(event_map: dict):
        for event in pygame.event.get(list(event_map.keys()), pump=False):
            event_func = event_map.get(event.type)
            if event_func:
                event_func(event=event)

    def make_event(self,
                   producer: EventUser,
                   consumer: EventUser,
                   data: dict):
        self.event_counts += 1

        event_id = f"{producer}:{consumer}"
        event_type = self.custom_event_types.get(event_id)
        if not event_type:
            event_type = pygame.event.custom_type()
            self.custom_event_types[event_id] = event_type
        return pygame.event.Event(event_type, data)

    def add_event(self,
                  producer: EventUser,
                  consumer: EventUser,
                  data: dict):
        pygame.event.post(self.make_event(producer, consumer, data))

    def get_event_data(self,
                   producer: EventUser,
                   consumer: EventUser) -> list:
        event_id = f"{producer}:{consumer}"
        event_type = self.custom_event_types.get(event_id)
        if event_type is None:
            return []
        return [x.dict for x in pygame.event.get(event_type)]

