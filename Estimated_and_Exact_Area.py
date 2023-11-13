import numpy as np
import time
import circumference


def Area_Calc(R, next_neighbor_distance):
    estimate_time_start = time.time_ns()
    isosceles_sides = R * np.ones(len(next_neighbor_distance))
    isosceles_heights = np.sqrt(np.square(isosceles_sides)-np.square(0.5*next_neighbor_distance))
    isosceles_areas = 0.5 * np.multiply(next_neighbor_distance, isosceles_heights)
    estimated_circle_area = np.sum(isosceles_areas)
    estimate_time_stop = time.time_ns()
    calculated_circle_area = np.pi*np.square(R)
    calculate_time_stop = time.time_ns()
    estimate_time_total = estimate_time_stop - estimate_time_start
    calculate_time_total = calculate_time_stop - estimate_time_stop
    print("The estimated area is: " + str(estimated_circle_area))
    print("The calculated area is: " + str(calculated_circle_area))
    print("The estimated area took " + str(estimate_time_total) + " seconds to calculate.")
    print("The exact area using pi took " + str(calculate_time_total) + " seconds to calculate.")

    return(estimated_circle_area, calculated_circle_area)


if __name__=="__main__":
    n = 100
    x = -1
    y = 10
    r = 5
    pts, x_pts, y_pts = circumference.create_point_array(x, y, r, n)
    next_neighbor = circumference.get_circumference(x_pts, y_pts, r)
    area = Area_Calc(r, next_neighbor)
