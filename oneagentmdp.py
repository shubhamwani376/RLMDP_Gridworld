import numpy as np
# import pandas as pd

from array import *


#red=-1, green=1, white=0, grey=-2

grid = np.array([[0, 0, 0, 0, -1],
     [0, -2, -2, 0, -1],
     [0, 0, 1, 0, -1],
     [0, -2, -2, 0, -1],
     [0, 0, 1, 0, -1]])

print(grid[1][1])
x=0
y=0
st=grid[x][y]

action=([0,0],[0,1],[0,-1],[1,0],[-1,0])#stay0,up1,down2,right3,left4
print (action[0][0])#---0

#input current state and action,
#output 2d array of probabilities of next state
def my_function(grid,action):
    for a in range(0,4)
     if x+action[a][0]<0 or x+action[a][0]>4 or y+action[a][1]<0 or y+action[a][1]>4
         a=0 #stay
     else stnext=grid[x+action[a][0]][y+action[a][1]]
    



my_function()
