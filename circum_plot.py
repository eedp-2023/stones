import matplotlib
import numpy as np
import math
import random
import matplotlib.pyplot as plt

def points(x=0, y=0, R=1, N=4, spacing=1):
    input_x = x
    input_y = y
    input_R = R
    input_N = N
    input_space = spacing  # 1=equally spaced, 2 = randomly spaced

    angle_x = []
    angle_y = []

    # Equally spaced
    if input_space == 1:
        space = 360 / input_N  # Divide by 360 degrees to find interval size
        interval_angle = []
        for i in range(0, input_N):  # Create list of increasing by interval value
            interval_angle.append(i * space)
        for deg in interval_angle:
            angle_x.append(math.cos(math.radians(deg)))
            angle_y.append(math.sin(math.radians(deg)))

    # Randomly Spaced
    if input_space == 2:
        random_angle = []
        for i in range(0, input_N):  # Random points between 0 and 360 degrees
            random_angle.append(random.randrange(0, 360))
        for deg in random_angle:
            angle_x.append(math.cos(math.radians(deg)))
            angle_y.append(math.sin(math.radians(deg)))

    # Converting to array and multiplying by radius size
    angle_x = input_R * np.array(angle_x)
    angle_y = input_R * np.array(angle_y)

    # Translating WRT Origin position
    angle_x = angle_x + input_x
    angle_y = angle_y + input_y

    # Creating the plot
    fig = plt.figure()
    ax = fig.add_subplot()
    circle1 = plt.Circle((input_x, input_y), radius=input_R, color='green', fill=False)
    tangent_points = plt.scatter(angle_x, angle_y)
    center_point = plt.plot(input_x, input_y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
    ax.add_patch(circle1)
    ax.axis('equal')
    if input_space == 1:
        plt.title("Equally Spaced")
    if input_space == 2:
        plt.title("Randomly Spaced")
    plt.show()
    return np.array(angle_x), np.array(angle_y)

# Test Case
# points_x, points_y = points(2.5,2.5, R =3.25, N = 10, spacing=2)

