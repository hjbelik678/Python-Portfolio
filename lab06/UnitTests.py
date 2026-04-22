import unittest
from P06SquareRoots import next_x, approximate_square_root


class MyTestCase(unittest.TestCase):
    def test_next_x(self):
        self.assertAlmostEqual(next_x(1, 2), 1.5)
        self.assertAlmostEqual(next_x(1.5, 2), 1.4166666666666667)
        self.assertAlmostEqual(next_x(1.4166666666666667, 2), 1.4142156862745097)
        self.assertAlmostEqual(next_x(1.4142156862745097, 2), 1.4142135623746899)
        self.assertAlmostEqual(next_x(1.4142135623746899, 2), 1.414213562373095)
        self.assertAlmostEqual(next_x(123, 5), 61.520325203252035)
        self.assertAlmostEqual(next_x(61.520325203252035, 5), 30.800799577970672)
        self.assertAlmostEqual(next_x(30.800799577970672, 5), 15.481566513039734)
        self.assertAlmostEqual(next_x(15.481566513039734, 5), 7.902265623171479)
        self.assertAlmostEqual(next_x(7.902265623171479, 5), 4.267497778193462)

    def test_approximate_square_root(self):
        self.assertAlmostEqual(approximate_square_root(2, 5), 1.414213562373095)
        self.assertAlmostEqual(approximate_square_root(5, 5), 2.23606797749979)
        self.assertAlmostEqual(approximate_square_root(1234, 10), 35.12833614050059)
        self.assertAlmostEqual(approximate_square_root(12345, 10), 111.10805770848404)
        self.assertAlmostEqual(approximate_square_root(12345, 20), 111.1080555135405)


if __name__ == '__main__':
    unittest.main()
