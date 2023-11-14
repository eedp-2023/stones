import random
import math
import numpy as np
import time


def find_y_coor(x, r):
  # random int decides whether y should be pos or negative
  y = math.sqrt((r ** 2) - (abs(x) ** 2))
  if random.random() < 0.5:
    # y ned
    y = -y

  return y

def create_point_array(x0, y0, r, n_pts):
  """Point array of circle returned in form [ (x0,y0), (x1,y1)... ] """
  x_rand_coor = [ random.uniform(-r, r) for i in range(n_pts) ]
  y_calc_coor = list(map(find_y_coor, x_rand_coor, [r for i in range(n_pts)]))
  array = [ (x+x0, y+y0) for x,y in zip(x_rand_coor, y_calc_coor) ]

  return array, x_rand_coor, y_calc_coor


def get_circumference(x_pts: np.array, y_pts: np.array, R, x0, y0):
  # Start Timer
  start_time = time.time_ns()

  x_pts = np.array(x_pts)
  y_pts = np.array(y_pts)
  # Sort points by angle to find next neighbor
  pt_angle = np.arctan2(y_pts-y0, x_pts-x0)
  pt_reshuffle_ind = np.argsort(pt_angle)
  x_pts = x_pts[pt_reshuffle_ind]
  y_pts = y_pts[pt_reshuffle_ind]
  pt_indexer = list(range(-1, len(x_pts) - 1))
  x_diff = x_pts - x_pts[pt_indexer]
  y_diff = y_pts - y_pts[pt_indexer]
  next_neighbor_distance = np.sqrt(x_diff ** 2 + y_diff ** 2)

  # print("Estimated Circumference: {:0.5f}".format(sum(next_neighbor_distance)))
  # print("Actual Circumference:    {:0.5f}".format(2 * np.pi * R))

  end_time = time.time_ns()

  print("Circumference Calculation Time: {0:.3f} us".format((end_time - start_time)/1e3))

  # Return [Next Neighbor Distance, Estimated Circumference, Actual Circumference]
  return next_neighbor_distance, sum(next_neighbor_distance), 2*np.pi*R


if __name__=="__main__":
  n = 100
  x = -1
  y = 10
  r = 5
  pts, x_pts, y_pts = create_point_array(x, y, r, n)
  num_repetitions = 1e4
  print("Timing {:.0f} Iterations".format(num_repetitions))
  st_time = time.time_ns()
  for i in range(int(num_repetitions)):
    next_neighbor = get_circumference(x_pts, y_pts, r)
  end_time = time.time_ns()
  print("Runtime: {:.3f} us".format((end_time-st_time)/1e3))
  print("Per call: {:.3f} us".format((end_time-st_time)/1e3/num_repetitions))
   # Mini Unit test to kick the tires
  '''
  num_test = 3
  R_test = 1
  ang = np.linspace(0, 2*np.pi*(1-1/num_test), num_test)
  x_test = R_test*np.sin(ang)
  y_test = R_test*np.cos(ang)
  nn = get_circumference(x_test, y_test, R_test)
  print("Fin")
  '''
