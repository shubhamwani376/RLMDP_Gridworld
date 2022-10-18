import numpy as np
from array import *
# import pandas as pd

#given current position(x, y), grid, action (stay=0, up=1, down=2, right=3, left=4), and p_e
#output 2d array of probabilities of next state
def stateEquation(x, y, grid, action, p_e):
    actions = np.array([[0,0],[0,1],[0,-1],[1,0],[-1,0]])
    probability = np.array([[0.0, 0.0, 0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0, 0.0, 0.0]])
    for i in range(0,5):
        if(i == action):
            if((x+actions[i][0])<0 or (x+actions[i][0])>4 or (y+actions[i][1])<0 or (y+actions[i][1])>4):
                probability[x][y]+=1-p_e
            else:
                probability[x+actions[i][0]][y+actions[i][1]] += 1-p_e
        else:
            if ((x+actions[i][0])<0 or (x+actions[i][0])>4 or (y+actions[i][1])<0 or (y+actions[i][1])>4):
                probability[x][y] += p_e/4
            else:
                probability[x+actions[i][0]][y+actions[i][1]] += p_e/4
    return probability

#red=-1, green=1, white=0, grey=-2
gridWorld = np.array([[0, 0, 0, 0, -1],
     [0, -2, -2, 0, -1],
     [0, 0, 1, 0, -1],
     [0, -2, -2, 0, -1],
     [0, 0, 1, 0, -1]])
actions = np.array([[0,0],[0,1],[0,-1],[-1,0],[0,1]])
x=y=0
                   
print(stateEquation(1,1,gridWorld,2,0.1))
