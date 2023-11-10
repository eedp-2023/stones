import numpy as np
from time import process_time
def Area_Calc(R, next_neighbor_distance):
    estimate_time_start = process_time()
    isosceles_sides = R * np.ones(len(next_neighbor_distance))
    isosceles_heights = np.sqrt(np.square(isosceles_sides)-np.square(0.5*next_neighbor_distance))
    isosceles_areas = 0.5 * np.multiply(next_neighbor_distance, isosceles_heights)
    estimated_circle_area = np.sum(isosceles_areas)
    estimate_time_stop = process_time()
    calculated_circle_area = np.pi*np.square(R)
    calculate_time_stop = process_time()
    estimate_time_total = estimate_time_stop - estimate_time_start
    calculate_time_total = calculate_time_stop - estimate_time_stop
    print("The estimated area is: " + str(estimated_circle_area))
    print("The calculated area is: " + str(calculated_circle_area))
    print("The estimated area took " + str(estimate_time_total) + " seconds to calculate.")
    print("The exact area using pi took " + str(calculate_time_total) + " seconds to calculate.")

test1 = np.array([4,2])

Area_Calc(3,test1)