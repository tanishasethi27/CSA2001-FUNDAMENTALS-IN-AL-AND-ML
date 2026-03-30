import matplotlib.pyplot as plt

def show_path(grid, path):
    plt.imshow(grid, cmap='gray')

    x = [p[1] for p in path]
    y = [p[0] for p in path]

    plt.plot(x, y)
    plt.title("Optimal Path")
    plt.show()
