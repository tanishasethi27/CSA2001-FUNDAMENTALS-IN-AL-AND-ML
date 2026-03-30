from environment.grid import create_grid
from search.astar import astar
from visualization.plot import show_path

def main():
    # Create environment
    grid, traffic = create_grid()
    
    # Define start and goal
    start = (0, 0)
    goal = (19, 19)

    # Run A* algorithm
    path = astar(grid, traffic, start, goal)

    # Visualize result
    show_path(grid, path)

if __name__ == "__main__":
    main()
