"""Djikstra's Path Finding"""

import pygame, sys, random, math
from collections import deque
from tkinter import messagebox, Tk

size = (width, height) = 640, 480
pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption("Dijktdtra's Path Finding")
clock = pygame.time.Clock()

cols, rows = 64//2, 48//2

w = width//cols
h = height//rows

grid = []
queue, visited = deque(), []
path = []

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        if (i+j)%7 == 0:
            self.wall == True
        
    def show(self, win, col, shape= 1):
        if self.wall == True:
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
        else:
            pygame.draw.circle(win, col, (self.x*w+w//2, self.y*h+h//2), w//3)
    
    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])
        #Add Diagonals


def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state



def dijikstra():
    
    for i in range(cols):
        arr = []
        for j in range(rows):
            arr.append(Spot(i, j))
        grid.append(arr)
        
    for i in range(cols):
        for j in range(rows):
            grid[i][j].add_neighbors(grid)

    start = grid[5][5]
    start.wall = False
    start.visited = True
    
    end = grid[cols - cols//2][rows - cols//4]
    end.wall = False

    queue.append(start)

    flag = False
    noflag = True
    startflag = False
    running_dijikstra = True
    
    ready_to_exit = False
    
    while running_dijikstra:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ready_to_exit and keys[pygame.K_RETURN]:
                running_dijikstra = False
            if keys[pygame.K_d]:
                    pos = pygame.mouse.get_pos()
                    grid[pos[0] // (width // cols )][pos[1]//(height//rows)].wall = False
            if not startflag:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if keys[pygame.K_s]:
                        start.visited = False
                        pos = pygame.mouse.get_pos()
                        start = grid[pos[0] // (width // cols )][pos[1]//(height//rows)]
                        start.wall = False
                        start.visited = True
                        queue.clear()
                        queue.append(start)
                    elif keys[pygame.K_e]:
                        pos = pygame.mouse.get_pos()
                        end = grid[pos[0] // (width // cols )][pos[1]//(height//rows)]
                        end.wall = False
                    elif event.button in (1, 3):  
                        clickWall(pygame.mouse.get_pos(), event.button==1)
                    
                        
                elif event.type == pygame.MOUSEMOTION:
                    if event.buttons[0] or event.buttons[2]:
                        clickWall(pygame.mouse.get_pos(), event.buttons[0])
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        startflag = True

        if startflag:   #Dijikstra Algorithm
            if len(queue) > 0:
                current = queue.popleft()
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not flag:
                        flag = True
                        Tk().wm_withdraw()
                        messagebox.showinfo("Path found", "shortest path found!!" )
                        print("Done")
                        ready_to_exit = True
                    elif flag:
                        continue
                if flag == False:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    noflag = False
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                    ready_to_exit = True
                else:
                    continue


        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, (44, 62, 80))
                if spot in path:
                    spot.show(win, (46, 204, 113))
                    spot.show(win, (192, 57, 43), 0)
                elif spot.visited:
                    spot.show(win, (39, 174, 96))
                if spot in queue and not flag:
                    spot.show(win, (44, 62, 80))
                    spot.show(win, (39, 174, 96), 0)
                if spot == start:
                    spot.show(win, (0, 255, 200))
                if spot == end:
                    spot.show(win, (0, 120, 255))
                
                
        pygame.display.update()


if __name__=="__main__":
    dijikstra()