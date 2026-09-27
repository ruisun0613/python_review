import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk
    # rw = RandomWalk()
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots()
    points_number = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c = points_number, s = 15, cmap = plt.cm.Blues, edgecolors = None)
    # ax.scatter(rw.x_values, rw.y_values, c = points_number, s = 1, cmap = plt.cm.Blues, edgecolors = None)

    # 15-3
    ax.plot(rw.x_values, rw.y_values, linewidth = 3)

    ax.set_aspect("equal")
    
    # Emphasize the starting and ending points.
    # ax.scatter(0, 0, c = 'green', edgecolors = None, s = 100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = None, s = 100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keeping_running = input("Make another walk (y/n):")
    if keeping_running == "n":
        break