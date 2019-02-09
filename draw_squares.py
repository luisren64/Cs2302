import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,10,p,.2)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

#Corner Squares Program
#Problem 1 Part a
def draw_squares(ax,n,p,size,mod):
    if n>0:
        bl = p[0]
        tl = p[1]
        tr = p[2]
        br = p[3]
        botleft = np.array([bl-size*mod,[bl[0]-size*mod,bl[1]+size*mod],bl+size*mod,[bl[0]+size*mod,bl[1]-size*mod],bl-size*mod])    
        topleft = np.array([tl-size*mod,[tl[0]-size*mod,tl[1]+size*mod],tl+size*mod,[tl[0]+size*mod,tl[1]-size*mod],tl-size*mod])
        topright = np.array([tr-size*mod,[tr[0]-size*mod,tr[1]+size*mod],tr+size*mod,[tr[0]+size*mod,tr[1]-size*mod],tr-size*mod])
        botright = np.array([br-size*mod,[br[0]-size*mod,br[1]+size*mod],br+size*mod,[br[0]+size*mod,br[1]-size*mod],br-size*mod])
        size = size * mod
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,botleft,size,mod)
        draw_squares(ax,n-1,topleft,size,mod)
        draw_squares(ax,n-1,topright,size,mod)
        draw_squares(ax,n-1,botright,size,mod)

plt.close("all") 
size = 10
p = np.array([[0,0],[0,size],[size,size],[size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,2,p,size,.25)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

#Problem 1 part b
def draw_squares(ax,n,p,size,mod):
    if n>0:
        bl = p[0]
        tl = p[1]
        tr = p[2]
        br = p[3]
        botleft = np.array([bl-size*mod,[bl[0]-size*mod,bl[1]+size*mod],bl+size*mod,[bl[0]+size*mod,bl[1]-size*mod],bl-size*mod])    
        topleft = np.array([tl-size*mod,[tl[0]-size*mod,tl[1]+size*mod],tl+size*mod,[tl[0]+size*mod,tl[1]-size*mod],tl-size*mod])
        topright = np.array([tr-size*mod,[tr[0]-size*mod,tr[1]+size*mod],tr+size*mod,[tr[0]+size*mod,tr[1]-size*mod],tr-size*mod])
        botright = np.array([br-size*mod,[br[0]-size*mod,br[1]+size*mod],br+size*mod,[br[0]+size*mod,br[1]-size*mod],br-size*mod])
        size = size * mod
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,botleft,size,mod)
        draw_squares(ax,n-1,topleft,size,mod)
        draw_squares(ax,n-1,topright,size,mod)
        draw_squares(ax,n-1,botright,size,mod)

plt.close("all") 
size = 10
p = np.array([[0,0],[0,size],[size,size],[size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,size,.25)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

#Problem 1 part c

def draw_squares(ax,n,p,size,mod):
    if n>0:
        bl = p[0]
        tl = p[1]
        tr = p[2]
        br = p[3]
        botleft = np.array([bl-size*mod,[bl[0]-size*mod,bl[1]+size*mod],bl+size*mod,[bl[0]+size*mod,bl[1]-size*mod],bl-size*mod])    
        topleft = np.array([tl-size*mod,[tl[0]-size*mod,tl[1]+size*mod],tl+size*mod,[tl[0]+size*mod,tl[1]-size*mod],tl-size*mod])
        topright = np.array([tr-size*mod,[tr[0]-size*mod,tr[1]+size*mod],tr+size*mod,[tr[0]+size*mod,tr[1]-size*mod],tr-size*mod])
        botright = np.array([br-size*mod,[br[0]-size*mod,br[1]+size*mod],br+size*mod,[br[0]+size*mod,br[1]-size*mod],br-size*mod])
        size = size * mod
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,botleft,size,mod)
        draw_squares(ax,n-1,topleft,size,mod)
        draw_squares(ax,n-1,topright,size,mod)
        draw_squares(ax,n-1,botright,size,mod)

plt.close("all") 
size = 10
p = np.array([[0,0],[0,size],[size,size],[size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,5,p,size,.25)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

#Branch Program
#Problem 3 Part a--------------------
def draw_squares(ax,n,p,size,mod):
    if n>0:
        new_orig_left = np.array([p[0]-size*(1-mod),p[0],[p[2][0]-size*(1+mod),p[2][1]-size*(1-mod)]])
        new_orig_right = np.array([p[2]-size*(1-mod),p[2],[p[2][0]+size*(1-mod),p[2][1]-size*(1-mod)]])
        ax.plot(p[:,0],p[:,1],color='k')
        
        size = size*(1-mod)
        draw_squares(ax,n-1,new_orig_left,size,mod)
        draw_squares(ax,n-1,new_orig_right,size,mod)

plt.close("all") 
size = 200
p = np.array([[-size,-size],[0,0],[size,-size]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,size,.4)
ax.set_aspect(1.5)
ax.axis('on')
plt.show()
fig.savefig('squares.png')

#Problem 3 part b-----------------
def draw_squares(ax,n,p,size,mod):
    if n>0:
        new_orig_left = np.array([p[0]-size*(1-mod),p[0],[p[2][0]-size*(1+mod),p[2][1]-size*(1-mod)]])
        new_orig_right = np.array([p[2]-size*(1-mod),p[2],[p[2][0]+size*(1-mod),p[2][1]-size*(1-mod)]])
        ax.plot(p[:,0],p[:,1],color='k')
        
        size = size*(1-mod)
        draw_squares(ax,n-1,new_orig_left,size,mod)
        draw_squares(ax,n-1,new_orig_right,size,mod)

plt.close("all") 
size = 200
p = np.array([[-size,-size],[0,0],[size,-size]])
fig, ax = plt.subplots()
draw_squares(ax,4,p,size,.5)
ax.set_aspect(1.5)
ax.axis('on')
plt.show()
fig.savefig('squares.png')

#Problem 3 part c--------------------

def draw_squares(ax,n,p,size,mod):
    if n>0:
        new_orig_left = np.array([p[0]-size*(1-mod),p[0],[p[2][0]-size*(1+mod),p[2][1]-size*(1-mod)]])
        new_orig_right = np.array([p[2]-size*(1-mod),p[2],[p[2][0]+size*(1-mod),p[2][1]-size*(1-mod)]])
        ax.plot(p[:,0],p[:,1],color='k')
        
        size = size*(1-mod)
        draw_squares(ax,n-1,new_orig_left,size,mod)
        draw_squares(ax,n-1,new_orig_right,size,mod)

plt.close("all") 
size = 200
p = np.array([[-size,-size],[0,0],[size,-size]])
fig, ax = plt.subplots()
draw_squares(ax,6,p,size,.5)
ax.set_aspect(1.5)
ax.axis('on')
plt.show()
fig.savefig('squares.png')