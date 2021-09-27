# Setup Python ----------------------------------------------- #
from dijikstra import dijikstra
from Astar import AStar
from mst import kruskal
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')

size = (width, height) = 640, 480

screen = pygame.display.set_mode(size,0,32)

font = pygame.font.SysFont(None, 50)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, width/2 - 80, 20)

        mx, my = pygame.mouse.get_pos()

       
        button_1 = pygame.Rect(width/2 - 40, 100, 200, 50)
        button_2 = pygame.Rect(width/2 - 40, 200, 200, 50)
        button_3 = pygame.Rect(width/2 - 40, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                dijikstra()
        if button_2.collidepoint((mx, my)):
            if click:
                AStar()
        if button_3.collidepoint((mx, my)):
            if click:
                kruskal()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Dijikstra',font,(255,255,0),screen,width/2 - 30,110)
        draw_text('AStar',font,(255,255,0),screen,width/2 - 30,210)
        draw_text('Kruskal',font,(255,255,0),screen,width/2 - 30,310)
        click = False
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

        pygame.display.update()
        mainClock.tick(60)


main_menu()