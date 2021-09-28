# Setup Python ----------------------------------------------- #
from dijikstra import dijikstra
from Astar import AStar
from mst import kruskal
from fft import fft

from utils import *

import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Vizulizer Menu')

size = (width, height) = 640, 480
screen = pygame.display.set_mode(size,0,32)

font = pygame.font.SysFont(None, 50)




def main_menu():
    
    start_pos = height//2 - 100
    gap = 50
    button_1 = Button(screen,"Dijikstra",location=(width//2 ,start_pos ),action=dijikstra,size=(160,30))
    button_2 = Button(screen,"AStar",location=(width//2 ,start_pos+gap ),action=AStar,size=(160,30))
    button_3 = Button(screen,"Curve smoothener",location=(width//2 ,start_pos + 2*gap  ),action=fft,size=(160,30))
    button_4 = Button(screen,"Minimum Spanning Tree",location=(width//2 ,start_pos  +3*gap),action=kruskal,size=(240,30))
    
    btns = [button_1,button_2,button_3,button_4]
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                check_btn_collide(btns)

        screen.fill((44, 62, 80))
        draw_text(screen,"MAIN MENU",pos=(width//2,50),color=WHITE,font_name="freesansbold.ttf",font_size=45)
        for btn in btns:
            btn.draw()

        
        pygame.display.update()
        mainClock.tick(60)


main_menu()