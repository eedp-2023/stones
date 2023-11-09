import numpy as np


def get_circumference(x_pts: np.array, y_pts: np.array, R):
    # Sort points by angle to find next neighbor
    pt_angle = np.arctan2(y_pts, x_pts)
    pt_reshuffle_ind = np.argsort(pt_angle)
    x_pts = x_pts[pt_reshuffle_ind]
    y_pts = y_pts[pt_reshuffle_ind]
    pt_indexer = list(range(-1, len(x_pts)-1))
    x_diff = x_pts - x_pts[pt_indexer]
    y_diff = y_pts - y_pts[pt_indexer]
    next_neighbor_distance = np.sqrt(x_diff**2 + y_diff**2)

    print("Estimated Circumference: {:0.5f}".format(sum(next_neighbor_distance)))
    print("Actual Circumference:    {:0.5f}".format(2*np.pi*R))
    return next_neighbor_distance


if __name__ == "__main__":  # Mini Unit test to kick the tires
    num_test = 3
    R_test = 1
    ang = np.linspace(0, 2*np.pi*(1-1/num_test), num_test)
    x_test = R_test*np.sin(ang)
    y_test = R_test*np.cos(ang)
    nn = get_circumference(x_test, y_test, R_test)
    print("Fin")
