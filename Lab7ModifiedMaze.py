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
import time
import queue

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

def BreadthFirstSearch(G,v):
    #This is the python adaptation of the psuedocode given to us by Dr. Fuentes
    visited = [False for i in range(len(G))]
    prev = [-1 for j in  range(len(G))]
    Q = queue.Queue(len(G))
    Q.put(v)
    visited[v] = True
    while not Q.empty():
        u = Q.get()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.put(t)
    return prev
    
def DepthFirstRecursive(G,source):
    #This is the python adaptation of the psuedocode given to us by Dr. Fuentes
    visited = [False for i in range(len(G))]
    prev = [-1 for j in  range(len(G))]
    visited[source] = True
    for t in G[source]:
        if not visited[t]:
            prev[t] = source
            DepthFirstRecursive(G,t)
    
    
def CreateAdjList(walls,rows,cols):
    #this method creates an adjacency list for a given maze. Numbers are not repeated.
    cells = rows * cols
    #Here we initialize a list the length of the cells.
    L = [[] for j in range(cells)]
    for i in range(0, cells-1): #Traversing the whole array except for the last cell, as it will remain empty due to no repeats.
        #This if Statement is specifically for the top row.
        #We only check if cells to the left are adjacent, since there are none above.
        if i >= cells - cols:
            #if there is no wall between current cell and the left, the adjacent cell is appended.
            if [i, i+1] not in walls:
                L[i].append(i+1)
        #This if statement is specifically for the far right row.
        #We only check cells above, since there are none to the left.
        elif (i + 1)% cols == 0:
            if [i, i+cols] not in walls:
                L[i].append(i+cols)
        else:
            if [i, i+1] not in walls:
                L[i].append(i+1)
            if [i, i+cols] not in walls:
                L[i].append(i+cols)
    return L
            
        
    
    
def MessagePrint(remove,cells):
    if remove < cells - 1:
        print('There may not be a path from source to destination.')
    elif remove == cells - 1:
        print('There is a unique path from source to destination.')
    else:
        print('There is at least one path from source to destination. There may be more.')
    return
        

def SameSet(Set,walls,d):
    #This method checks if two cells are in the same set.
    i = int(walls[d][0])
    j = int(walls[d][1])
    #The find method is used to check the root of two cells.
    #If they are the same, it returns true. If not, it returns false.
    if dsf.find_c(Set,i) == dsf.find(Set,j):
        return True
    else:
        return False
              
def RemoveWalls(Set,walls,cells,remove):
    count = 0
    while count < remove:
        #Here we choose a random wall
        d = random.randint(0,len(walls)-1)
        #We check if cells are in the same set until count surpasses cells -1,
        #Which is when we remove random walls since a path is already guaranteed to exist.
        if count < (cells - 1):
            #If the cells are not in the same set, we remove the wall keeping them apart.
            
            if SameSet(Set,walls,d) == False:
                dsf.union_c(Set,walls[d][0],walls[d][1])
                walls.pop(d)
                count = count + 1
        else:
            walls.pop(d)
            count = count + 1
    return


plt.close("all") 
maze_rows = 3
maze_cols = 3
n = maze_rows * maze_cols
walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

#This creates a dsf the same size as the number of cells
Set = dsf.DisjointSetForest(n)

print('There are ', n, ' cells in the maze. How many walls would you like to remove?')
m = int(input())

MessagePrint(m,n)

#tStart = time.time()
RemoveWalls(Set,walls,n,m)
#endTime = time.time() - tStart
draw_maze(walls,maze_rows,maze_cols)
#print(endTime)
L = CreateAdjList(walls,maze_rows,maze_cols)
print(L)
Sol = BreadthFirstSearch(L,0)
print(Sol)

 