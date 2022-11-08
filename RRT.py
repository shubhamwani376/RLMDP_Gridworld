import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def RRT()
fig, ax = plt.subplots()

if __name__ == "__main__":
    start_pos = np.array([0.25,0.25,0]);
    end_pos = np.array([0.75,0.75,np.pi]);
    step_size = 0.1;
    node_max = 2000;
    threshold = 0.05;
    path_found = 0; # boolean
    path,path_found = RRT( start_pos, end_pos, step_size,threshold,node_max, path_found )


