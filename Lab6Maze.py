#Luis Renteria
#Olac Fuentes
#M/W 1:30 - 2:50

# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import dsf

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w


def CheckSet(M):
    #This method checks if there is only 1 set.
    #If all cells are in 1 set, the length of the dsf list should be one.
    #If the length is more tham one, all cells are not part of the same set.
    if len(dsf.dsfToSetList(M)) > 1:
        return False
    return True

def SameSet(Set,walls,d):
    #This method checks if two cells are in the same set.
    i = int(walls[d][0])
    j = int(walls[d][1])
    #The find method is used to check the root of two cells.
    #If they are the same, it returns true. If not, it returns false.
    if dsf.find(Set,i) == dsf.find(Set,j):
        return True
    else:
        return False
              
def RemoveWalls(Set,walls):
    #This method removes walls until all celss are part of the same set.
    while CheckSet(M) is not True:
        #Here we choose a random wall
        d = random.randint(0,len(walls)-1)
        #If the cells are not in the same set, we remove the wall keeping them apart.
        if SameSet(Set,walls,d) == False:
            #NOTE: For this particular submission, I used union without compression.
            dsf.union(Set,walls[d][0],walls[d][1])
            walls.pop(d)
    return


plt.close("all") 
maze_rows = 10
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

#This creates a dsf the same size as the number of cells
M = dsf.DisjointSetForest(maze_rows * maze_cols)

RemoveWalls(M,walls)

draw_maze(walls,maze_rows,maze_cols) 