import pygame

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Button():
    def __init__(self,window, txt, location, action, bg=WHITE, fg=BLACK, size=(80, 30), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
     
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)
        self.window = window
        
        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        self.window.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # mouseover color

    def call_back(self):
        self.call_back_()


def check_btn_collide(buttons):
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(pos):
            button.call_back()



def draw_text(surface,text,pos, font_name="Segoe Print", color=BLACK,font_size=16):
    font = pygame.font.SysFont(font_name, font_size)
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = pos
    surface.blit(textobj, textrect)