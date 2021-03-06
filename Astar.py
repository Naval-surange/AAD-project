import pygame, sys, random, math
from tkinter import messagebox, Tk



size = (width, height) = 640, 480

cols, rows = 64//2, 48//2


grid = []
openSet, closeSet = [], []
path = []

w = width//cols
h = height//rows

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        # if random.randint(0, 100) < 20:
        #     self.wall = True
        
    def show(self, win, col):
        if self.wall == True:
            col = (0, 0, 0)
        pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
    
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
        if self.x < cols - 1 and self.y < rows - 1:
            self.neighbors.append(grid[self.x+1][self.y+1])
        if self.x < cols - 1 and self.y > 0:
            self.neighbors.append(grid[self.x+1][self.y-1])
        if self.x > 0 and self.y < rows - 1:
            self.neighbors.append(grid[self.x-1][self.y+1])
        if self.x > 0 and self.y > 0:
            self.neighbors.append(grid[self.x-1][self.y-1])


def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state

def place(pos):
    i = pos[0] // w
    j = pos[1] // h
    return w, h
            
def heuristics(a, b):
    return math.sqrt((a.x - b.x)**2 + abs(a.y - b.y)**2)


for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)



def close():
    pygame.quit()
    sys.exit()


def AStar():
    pygame.init()

    win = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    fps = 30

    start = grid[cols//2][5]
    end = grid[cols//2][cols - cols//2]

    openSet.append(start)

    flag = False
    noflag = True
    startflag = False
    running_AStar = True
    ready_to_exit = False
    
    while running_AStar:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ready_to_exit and keys[pygame.K_RETURN]:
                running_AStar = False
            if keys[pygame.K_d]:
                pos = pygame.mouse.get_pos()
                grid[pos[0] // (width // cols )][pos[1]//(height//rows)].wall = False
            if not startflag:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if keys[pygame.K_s]:
                        pos = pygame.mouse.get_pos()
                        start = grid[pos[0] // (width // cols )][pos[1]//(height//rows)]
                        start.wall = False
                        start.visited = True
                        openSet.clear()
                        openSet.append(start)
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

        if startflag:   #AStar algorithm
            if len(openSet) > 0:
                winner = 0
                for i in range(len(openSet)):
                    if openSet[i].f < openSet[winner].f:
                        winner = i

                current = openSet[winner]
                
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
                    openSet.remove(current)
                    closeSet.append(current)

                    for neighbor in current.neighbors:
                        if neighbor in closeSet or neighbor.wall:
                            continue
                        tempG = current.g + 1

                        newPath = False
                        if neighbor in openSet:
                            if tempG < neighbor.g:
                                neighbor.g = tempG
                                newPath = True
                        else:
                            neighbor.g = tempG
                            newPath = True
                            openSet.append(neighbor)
                        
                        if newPath:
                            neighbor.h = heuristics(neighbor, end)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.prev = current

            else:
                if noflag:
                    noflag = False
                    ready_to_exit = True 
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                   

        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, (44, 62, 80))
                if flag and spot in path:
                    spot.show(win, (25, 120, 250))
                elif spot in closeSet:
                    spot.show(win, (255, 0, 0))
                elif spot in openSet:
                    spot.show(win, (0, 255, 0))
                try:
                    if spot == end:
                        spot.show(win, (0, 120, 255))
                except Exception:
                    pass
        clock.tick(fps)
        pygame.display.flip()



if __name__=="__main__":
    AStar()