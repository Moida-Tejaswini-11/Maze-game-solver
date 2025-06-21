import numpy as np
import matplotlib.pyplot as plt

maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

start = (int(input("start_row")), int(input("start_col")))
end = (int(input("end_row")), int(input("end_row")))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solvemaze(maze, start, end, path=[]):
    x, y = start
    if start == end:
        return path + [end]
    
    maze[x, y] = 2
    path.append(start)

    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if 0 <= new_x < maze.shape[0] and 0 <= new_y < maze.shape[1] and maze[new_x, new_y] == 0:
            result = solvemaze(maze.copy(), (new_x, new_y), end, path.copy())
            if result:
                return result
    return None

solution = solvemaze(maze.copy(), start, end)

def plot_maze(maze, solution):
    plt.imshow(maze, cmap='binary')
    plt.xticks([]), plt.yticks([])

    if solution:
        x_coords, y_coords = zip(*solution)
        plt.plot(y_coords, x_coords, color='red', linewidth=2, label='Solution Path')

    plt.legend()
    plt.show()

plot_maze(maze, solution)
