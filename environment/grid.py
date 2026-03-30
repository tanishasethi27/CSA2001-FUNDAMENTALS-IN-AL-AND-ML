import numpy as np
import random

def create_grid():
    grid = np.zeros((20, 20))

    # Obstacles
    for _ in range(40):
        x, y = random.randint(0,19), random.randint(0,19)
        grid[x][y] = 1

    # Traffic probability map
    traffic = np.random.uniform(0, 0.8, (20, 20))

    return grid, traffic
