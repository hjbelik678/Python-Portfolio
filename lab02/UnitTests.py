import unittest
import P01DayOfTheWeek
import P02AreasOfRectangles
import P03TimeCalculator
import P04LeapYear
import P05NumberOfRoots
import P06WhatIsMyGrade
import P07WhatDoINeedOnTheFinal


class MyTestCase(unittest.TestCase):
    def test_day_of_week(self):
        for item in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]):
            self.assertEqual(item[1], P01DayOfTheWeek.day_of_week(item[0] + 1))

        for number in range(8, 101):
            self.assertEqual("Error", P01DayOfTheWeek.day_of_week(number))

        for number in range(0, -101, -1):
            self.assertEqual("Error", P01DayOfTheWeek.day_of_week(number))

    def test_area(self):
        for w in range(1, 101, 5):
            for h in range(1, 101, 3):
                self.assertEqual(w * h, P02AreasOfRectangles.area_of_rectangle(w, h))

    def test_areas_of_rectangles(self):
        for a1 in range(10, 100, 3):
            for a2 in range(a1 - 1, 1, -5):
                self.assertEqual("The first rectangle is larger.", P02AreasOfRectangles.result(a1, a2))
                self.assertEqual("The second rectangle is larger.", P02AreasOfRectangles.result(a2, a1))
        for a in range(1, 101, 7):
            self.assertEqual("The rectangles have the same area.", P02AreasOfRectangles.result(a, a))

    def test_leap_year(self):
        for year in [2000, 2008, 2020, 2400, 2024, 2028, 2032]:
            self.assertEqual("That year is a leap year.", P04LeapYear.is_leap_year(year))
        for year in [1800, 1900, 2100, 2200, 2300, 2500, 2022, 2021, 2009, 2023, 2025]:
            self.assertEqual("That year is not a leap year.", P04LeapYear.is_leap_year(year))
        for year in range(0, -101, -1):
            self.assertEqual("Year must be positive.", P04LeapYear.is_leap_year(year))

    def test_number_of_roots(self):
        self.assertEqual(0, P05NumberOfRoots.number_of_roots(4, 12, 10))
        self.assertEqual(0, P05NumberOfRoots.number_of_roots(-3, 2, -1))
        self.assertEqual(0, P05NumberOfRoots.number_of_roots(3, 4, 25))
        self.assertEqual(1, P05NumberOfRoots.number_of_roots(1, 6, 9))
        self.assertEqual(1, P05NumberOfRoots.number_of_roots(-3, 6, -3))
        self.assertEqual(1, P05NumberOfRoots.number_of_roots(1, 8, 16))
        self.assertEqual(2, P05NumberOfRoots.number_of_roots(1, -3, 2))
        self.assertEqual(2, P05NumberOfRoots.number_of_roots(1, 5, 4))
        self.assertEqual(2, P05NumberOfRoots.number_of_roots(4, 19, -5))

    def test_time(self):
        self.assertEqual("14 day(s), 6 hour(s), 56 minute(s), and 7 second(s)",
                         P03TimeCalculator.seconds_to_time(1234567))
        self.assertEqual("9 hour(s), 36 minute(s), and 7 second(s)",
                         P03TimeCalculator.seconds_to_time(34567))
        self.assertEqual("16 minute(s) and 27 second(s)",
                         P03TimeCalculator.seconds_to_time(987))
        self.assertEqual("13 second(s)",
                         P03TimeCalculator.seconds_to_time(13))
        self.assertEqual("1 day(s), 0 hour(s), 0 minute(s), and 0 second(s)",
                         P03TimeCalculator.seconds_to_time(86400))
        self.assertEqual("1 hour(s), 0 minute(s), and 0 second(s)",
                         P03TimeCalculator.seconds_to_time(3600))
        self.assertEqual("1 minute(s) and 0 second(s)",
                         P03TimeCalculator.seconds_to_time(60))
        self.assertEqual("1 second(s)",
                         P03TimeCalculator.seconds_to_time(1))
        self.assertEqual("0 second(s)",
                         P03TimeCalculator.seconds_to_time(0))

    def test_letter_grade(self):
        self.assertEqual("A", P06WhatIsMyGrade.letter_grade(100))
        self.assertEqual("A", P06WhatIsMyGrade.letter_grade(95))
        self.assertEqual("A", P06WhatIsMyGrade.letter_grade(90))
        self.assertEqual("B", P06WhatIsMyGrade.letter_grade(89.99))
        self.assertEqual("B", P06WhatIsMyGrade.letter_grade(89))
        self.assertEqual("B", P06WhatIsMyGrade.letter_grade(85))
        self.assertEqual("B", P06WhatIsMyGrade.letter_grade(80))
        self.assertEqual("C", P06WhatIsMyGrade.letter_grade(79.99))
        self.assertEqual("C", P06WhatIsMyGrade.letter_grade(79))
        self.assertEqual("C", P06WhatIsMyGrade.letter_grade(75))
        self.assertEqual("C", P06WhatIsMyGrade.letter_grade(70))
        self.assertEqual("D", P06WhatIsMyGrade.letter_grade(69.99))
        self.assertEqual("D", P06WhatIsMyGrade.letter_grade(69))
        self.assertEqual("D", P06WhatIsMyGrade.letter_grade(65))
        self.assertEqual("D", P06WhatIsMyGrade.letter_grade(55))
        self.assertEqual("F", P06WhatIsMyGrade.letter_grade(54.99))
        self.assertEqual("F", P06WhatIsMyGrade.letter_grade(40))
        self.assertEqual("F", P06WhatIsMyGrade.letter_grade(30))
        self.assertEqual("F", P06WhatIsMyGrade.letter_grade(0))

    def test_final_grade(self):
        for grade in range(0, 101, 10):
            self.assertAlmostEqual(grade, P06WhatIsMyGrade.final_average(grade, grade, grade, grade, grade), 2)
        self.assertAlmostEqual(79.50, P06WhatIsMyGrade.final_average(100, 90, 80, 70, 60), 2)
        self.assertAlmostEqual(80.50, P06WhatIsMyGrade.final_average(60, 70, 80, 90, 100), 2)
        self.assertAlmostEqual(80.50, P06WhatIsMyGrade.final_average(60, 70, 80, 90, 100), 2)
        self.assertAlmostEqual(89.20, P06WhatIsMyGrade.final_average(92, 84, 82, 95, 97), 2)

    def test_grade_needed_on_final(self):
        self.assertAlmostEqual(84.67, P07WhatDoINeedOnTheFinal.grade_needed_on_final(92, 84, 95, 97, 90), 2)
        self.assertAlmostEqual(51.33, P07WhatDoINeedOnTheFinal.grade_needed_on_final(92, 84, 95, 97, 80), 2)
        self.assertAlmostEqual(18.00, P07WhatDoINeedOnTheFinal.grade_needed_on_final(92, 84, 95, 97, 70), 2)
        self.assertAlmostEqual(-32.00, P07WhatDoINeedOnTheFinal.grade_needed_on_final(92, 84, 95, 97, 55), 2)
        self.assertAlmostEqual(9.17, P07WhatDoINeedOnTheFinal.grade_needed_on_final(70, 65, 80, 80, 55), 2)
        self.assertAlmostEqual(59.17, P07WhatDoINeedOnTheFinal.grade_needed_on_final(70, 65, 80, 80, 70), 2)
        self.assertAlmostEqual(92.50, P07WhatDoINeedOnTheFinal.grade_needed_on_final(70, 65, 80, 80, 80), 2)
        self.assertAlmostEqual(125.83, P07WhatDoINeedOnTheFinal.grade_needed_on_final(70, 65, 80, 80, 90), 2)


if __name__ == '__main__':
    unittest.main()
