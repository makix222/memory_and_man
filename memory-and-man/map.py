import pygame
import json
import uuid
from datetime import datetime
from pathlib import Path

class Maps:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface(size=(width, height))
        self.wall_color = (30, 11, 14)
        self.map_dir = Path('maps')
        self.draw_objects = {"rect": [],
                             "circle": [],
                             "polygon": [],
                             "ellipse": [],
                             "arc": [],
                             "line": [],
                             "lines": []}
        self.draw_map = {"rect": self.draw_rect,
                         "circle": self.draw_circle,
                         "polygon": self.draw_polygon,
                         "ellipse": self.draw_ellipse,
                         "arc": self.draw_arc,
                         "line": self.draw_line,
                         "lines": self.draw_lines}
        self.machine_code = uuid.getnode()

    def load_map(self, map_file):
        with (self.map_dir / map_file).open() as map_object:
            self.draw_objects = json.load(fp=map_object)

    def save_map(self):
        with Path(f'{self.machine_code}_{datetime.now().isoformat()}.map') as output_file:
            json.dump(obj=self.draw_objects, fp=output_file)

    def draw_shapes(self):
        for k, v in self.draw_objects:
            for parameters in v:
                self.draw_map[k](parameters)

    def draw_rect(self, parameters):
        pygame.draw.rect(self.surface,
                         **parameters)
        
    def draw_circle(self, parameters):
        pygame.draw.circle(self.surface,
                         **parameters)
        
    def draw_polygon(self, parameters):
        pygame.draw.polygon(self.surface,
                         **parameters)
        
    def draw_ellipse(self, parameters):
        pygame.draw.ellipse(self.surface,
                         **parameters)
        
    def draw_arc(self, parameters):
        pygame.draw.arc(self.surface,
                         **parameters)
        
    def draw_line(self, parameters):
        pygame.draw.line(self.surface,
                         **parameters)
        
    def draw_lines(self, parameters):
        pygame.draw.lines(self.surface,
                         **parameters)
        
