import unittest
import numpy as np
from math import sqrt
# from random import seed

from circum_plot import points
from circumference import get_circumference
from Estimated_and_Exact_Area import Area_Calc


class stonesTestCase(unittest.TestCase):

    def test_pt_generation(self):

        # equally spaced points, n=4
        x1 = 0; y1 = 0; R1 = 1; n1 = 4
        xout1, yout1 = points(x1, y1, R1, n1, 1)
        self.assertTrue(np.allclose(xout1, np.array([1., 0., -1., 0.])))
        self.assertTrue(np.allclose(yout1, np.array([0., 1., 0., -1.])))

        # non-centered points, n=3
        x2 = 1; y2 = -1; R2 = 2; n2 = 3
        xout2, yout2 = points(x2, y2, R2, n2, 1)
        self.assertTrue(np.allclose(xout2, np.array([3., 0., 0.])))
        self.assertTrue(np.allclose(yout2, np.array([-1., 2*sqrt(0.75)-1, -2*sqrt(0.75)-1])))

        # seed(1)
        # random points, check all points are on circle
        x3 = 0; y3 = 0; R3 = 5; n3 = 5
        xout3, yout3 = points(x3, y3, R3, n3, 2)
        self.assertTrue(np.allclose(np.sqrt(np.square(xout3 - x3) + np.square(yout3 - y3))), R3)


    def test_circumference(self):

        # centered square
        x1 = np.array([0, -sqrt(2), 0, sqrt(2)])
        y1 = np.array([sqrt(2), 0, -sqrt(2), 0])
        out1 = np.array([2., 2., 2., 2.])
        self.assertTrue(np.allclose(get_circumference(x1, y1, sqrt(2)), out1))

        # non-centered square @ (1,1)
        x2 = np.array([1, 1-sqrt(2), 1, 1+sqrt(2)])
        y2 = np.array([1+sqrt(2), 1, 1-sqrt(2), 1])
        out2 = np.array([2., 2., 2., 2.])
        self.assertTrue(np.allclose(get_circumference(x2, y2, sqrt(2)), out2))

        # centered square, differently ordered pts
        x3 = np.array([0,  0, -sqrt(2), sqrt(2)])
        y3 = np.array([-sqrt(2), sqrt(2), 0, 0])
        out3 = np.array([2., 2., 2., 2.])
        self.assertTrue(np.allclose(get_circumference(x3, y3, sqrt(2)), out3))

        # unequally spaced pts, rectangle
        x4 = np.array([0.5, -0.5, -0.5, 0.5])
        y4 = np.array([sqrt(0.75), sqrt(0.75), -sqrt(0.75), -sqrt(0.75)])
        out4 = np.array([2*sqrt(0.75), 1., 2*sqrt(0.75), 1.]) # order manually checked
        self.assertTrue(np.allclose(get_circumference(x4, y4, 1), out4))

    def test_area(self):

        # square
        in1 = np.array([2., 2., 2., 2.])
        R1 = sqrt(2)
        out1 = 4
        self.assertTrue(np.allclose(Area_Calc(R1, in1), out1))

        # pentagon
        in2 = np.array([1., 1., 1., 1., 1.])
        R2 = 0.75
        out2 = sqrt((0.75**2)-(0.5**2)) * 2.5
        self.assertTrue(np.allclose(Area_Calc(R2, in2), out2))

        # unequally spaced pts, rectangle
        in3 = np.array([2*sqrt(0.75), 1., 2*sqrt(0.75), 1.])
        R3 = 1.0
        out3 = 2*sqrt(0.75)
        self.assertTrue(np.allclose(Area_Calc(R3, in3), out3))



if __name__ == '__main__':

    stonesTestCase.main()
