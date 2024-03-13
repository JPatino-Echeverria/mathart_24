import numpy as np
import matplotlib.pyplot as plt

# Define the transformation functions and their probabilities
def f1(x, y):
    return 0, 0.16*y

def f2(x, y):
    return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6

def f3(x, y):
    return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6

def f4(x, y):
    return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

functions = [f1, f2, f3, f4]
probabilities = [0.01, 0.85, 0.07, 0.07]

# Initialize points and the figure
x, y = 0, 0
points = []

for _ in range(500000):  # Increase number of points for better detail
    f = np.random.choice(functions, p=probabilities)
    x, y = f(x, y)
    points.append((x, y))

# Convert points to colours based on their y position
max_y = max(points, key=lambda item: item[1])[1]
colors = [plt.cm.rainbow(y/max_y) for x, y in points]

# Create the plot 
fig, ax = plt.subplots(figsize=(23.4, 33.1), dpi=300)  # A1 size at 300 DPI
ax.scatter(*zip(*points), s=0.1, color=colors, marker='.')
ax.axis('off')
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Save the image
plt.savefig('fern_rainbow_transparentbackground.png', dpi=300, bbox_inches='tight', pad_inches=0, transparent=True)
plt.close()

