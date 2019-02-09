import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#Problem 1-------------------------
#Problem 1 Part a
def draw_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[radius*3/5,0],radius*(3/5))
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')

#-----------------------------------
#Problem 1 Part b
def draw_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[radius*8/9,0],radius*(8/9))
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')

#------------------------------------
#Problem 1 Part c

def draw_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[radius*19/20,0],radius*(19/20))
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')

#Problem 4------------------------ Incomplete
#Problem 4 Part a
def draw_circles(ax,n,center,radius,w,xcord):
    
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        #Smaller center circle
        draw_circles(ax,n-1,center,radius*w,w,xcord)
        #Smaller top circle
        draw_circles(ax,n-1,[xcord,radius*2*w],radius*w,w,-m*xcord+(radius*2*w))
        #Smaller bottom circle
        draw_circles(ax,n-1,[-xcord,-radius*2*w],radius*w,w,-m*xcord+(radius*2*w))
        #Smaller left circle
        draw_circles(ax,n-1,[-radius*2*w,-xcord],radius*w,w,-m*xcord+(radius*2*w))
        #Smaller right circle
        draw_circles(ax,n-1,[radius*2*w,xcord],radius*w,w,-m*xcord+(radius*2*w))
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, [0,0], 100,1/3,0)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')



