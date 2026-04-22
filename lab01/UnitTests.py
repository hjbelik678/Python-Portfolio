"""
Test cases for Lab01. Do not edit.
"""
import unittest
from unittest.mock import patch
from io import StringIO
import P01LandCalculation
import P02MilesPerGallon
import P03TemperatureConverter
import P04ArrivalTime
import P05CompoundInterest


class TestLab01(unittest.TestCase):
    def test_land_calculation(self):
        for test_value in range(0, 1000):
            self.assertEqual(test_value, P01LandCalculation.land_calculation(43560 * test_value))
            self.assertEqual(test_value, P01LandCalculation.land_calculation(43560 * test_value + 1))
            self.assertEqual(test_value, P01LandCalculation.land_calculation(43560 * (test_value + 1) - 1))

    def test_mpg(self):
        self.assertEqual(10, P02MilesPerGallon.mpg(100, 10))
        self.assertEqual(10, P02MilesPerGallon.mpg(109, 10))
        for test_value in range(10, 100):
            for gallons in range(13, 25):
                self.assertEqual(test_value, P02MilesPerGallon.mpg(gallons*test_value, gallons))

    def test_temperature_converter(self):
        self.assertEqual(-40.0, P03TemperatureConverter.celsius_to_fahrenheit(-40))
        self.assertEqual(32.0, P03TemperatureConverter.celsius_to_fahrenheit(0))
        self.assertEqual(212.0, P03TemperatureConverter.celsius_to_fahrenheit(100))
        self.assertEqual(89.6, P03TemperatureConverter.celsius_to_fahrenheit(32))
        self.assertEqual(105.8, P03TemperatureConverter.celsius_to_fahrenheit(41))

    def assertTime(self, distance, speed, hours, minutes):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P04ArrivalTime.print_arrival_time(distance, speed)
            self.assertEqual("Arrival in %d hour(s) and %d minute(s)\n" % (hours, minutes), mock_out.getvalue())

    def test_arrival_time(self):
        self.assertTime(1, 60, 0, 1)
        self.assertTime(1, 61, 0, 0)
        self.assertTime(120, 60, 2, 0)
        self.assertTime(121, 60, 2, 1)
        self.assertTime(500, 60, 8, 20)
        self.assertTime(500, 45, 11, 6)
        self.assertTime(700, 73, 9, 35)

    def test_compound_interest(self):
        self.assertAlmostEqual(200.50, P05CompoundInterest.future_value(200.50, 0, 10, 3), places=2)
        self.assertAlmostEqual(23152.50, P05CompoundInterest.future_value(20000, 5, 1, 3), places=2)
        self.assertAlmostEqual(11616.17, P05CompoundInterest.future_value(10000, 3, 12, 5), places=2)
        self.assertAlmostEqual(10407.07, P05CompoundInterest.future_value(10000, 2, 4, 2), places=2)


if __name__ == '__main__':
    unittest.main()
