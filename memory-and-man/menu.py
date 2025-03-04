import pygame

class Menus:
    def __init__(self):
        self.menus = []

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.name = ""

class MenuElement:
    def __init__(self,
                 surface: pygame.Surface,
                 click_func,
                 click_func_args,
                 size=(20, 20),
                 center_pos=(0,0),
                 color=(100, 100, 100),
                 text_color=(250, 250, 250)):

        self.surface = surface
        self.func = click_func
        self.func_args = click_func_args

        self.exists = False
        self.rect = None

        self.size = size
        self.center = center_pos

        self.color = color
        self.text_color = text_color
        self.border_color = (140, 140, 140)

        self.border_width = 2
        self.border_radius = 2
        self.text = self.set_text("Menu Element")
        self.text_size = 12
    
    def set_text(self, text):
        font_str = "verdana"
        system_fonts = pygame.font.get_fonts()
        if font_str not in system_fonts:
            font_str = pygame.font.get_default_font()
        font_path = pygame.font.match_font(font_str)
        if font_path is None:
            raise SystemError(f'Unable to find {font_str} or a default font.')
        font_obj = pygame.font.Font(font_path,
                                    self.text_size)
        return font_obj.render(text,
                               True,
                               self.text_color,
                               background=self.color)

    def click(self):
        self.func(self.func_args)

    def draw(self):
        if not self.exists:
            self.rect = pygame.Rect((self.center[0] - self.size[0]/2, self.center[1] - self.size[1]/2),
                               self.size)

        pygame.draw.rect(self.surface,
                         self.color,
                         self.rect,
                         0,
                         self.border_radius)

        pygame.draw.rect(self.surface,
                         self.border_color,
                         self.rect,
                         self.border_width,
                         self.border_radius)

        self.surface.blit()




