import unittest
import random # seed
import numpy as np
from math import sqrt

from area import *
from circumference import get_circumference
from circum_plot import *
from Estimated_and_Exact_Area import Area_Calc


class stonesTestCase(unittest.TestCase):

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
        print(get_circumference(x4, y4, 1))
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
