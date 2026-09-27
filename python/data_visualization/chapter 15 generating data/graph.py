"""
15-1. Cubes: A number raised to the third power is a cube. Plot the first
five cubic numbers, and then plot the first 5,000 cubic numbers.
15-2. Colored Cubes: Apply a colormap to your cubes plot.
"""
import matplotlib.pyplot as plt

# 15-1
# first five cubic numbers figure
first_five_number = (1, 2, 3, 4, 5)
first_five_number_cube = [x ** 3 for x in first_five_number]

plt.scatter(first_five_number, first_five_number_cube, s = 10, color = 'blue')
plt.show()

# first 5000
five_thousand_number = range(1, 5000)
five_thousand_cube = [z ** 3 for z in five_thousand_number]

plt.scatter(five_thousand_number, five_thousand_cube, c = five_thousand_cube, cmap = plt.cm.Reds, s = 10)
plt.show()