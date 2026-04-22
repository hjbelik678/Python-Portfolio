import unittest
from unittest.mock import patch
from io import StringIO
import P01PrintingStars
import P02ApproximatePi
import P03DigitSum
import P04MaybeFinite
import P06MoreGuessing


class MyTestCase(unittest.TestCase):
    def test_print_stars(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.print_stars(0)
            self.assertEqual("", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.print_stars(1)
            self.assertEqual("*\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.print_stars(2)
            self.assertEqual("*\n**\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.print_stars(3)
            self.assertEqual("*\n**\n***\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.print_stars(4)
            self.assertEqual("*\n**\n* *\n****\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.print_stars(5)
            self.assertEqual("*\n**\n* *\n*  *\n*****\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.print_stars(6)
            self.assertEqual("*\n**\n* *\n*  *\n*   *\n******\n", mock_out.getvalue())

    def test_echo_print(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01PrintingStars.echo_print("bob", 0)
            self.assertEqual("", mock_out.getvalue())
        for i in range(1, 11):
            with patch('sys.stdout', new=StringIO()) as mock_out:
                P01PrintingStars.echo_print("bob", i)
                self.assertEqual("bob" * i, mock_out.getvalue())

    def test_digit_sum(self):
        self.assertEqual(6, P03DigitSum.digit_sum(123))
        self.assertEqual(6, P03DigitSum.digit_sum(-123))
        self.assertEqual(45, P03DigitSum.digit_sum(1234567890))
        self.assertEqual(45, P03DigitSum.digit_sum(-1234567890))
        self.assertEqual(45, P03DigitSum.digit_sum(987654321))
        self.assertEqual(45, P03DigitSum.digit_sum(-987654321))
        for i in range(10):
            self.assertEqual(i, P03DigitSum.digit_sum(i))
            self.assertEqual(i, P03DigitSum.digit_sum(-i))
            self.assertEqual(i, P03DigitSum.digit_sum(i * 100))
            self.assertEqual(i, P03DigitSum.digit_sum(-i * 100))

    def test_maybe_finite(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P04MaybeFinite.print_sequence(1)
            self.assertEqual("1\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P04MaybeFinite.print_sequence(2)
            self.assertEqual("2, 1\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P04MaybeFinite.print_sequence(26)
            self.assertEqual("26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1\n", mock_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P04MaybeFinite.print_sequence(27)
            self.assertEqual("27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, "
                             "91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, "
                             "1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, "
                             "850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, "
                             "7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, "
                             "1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, "
                             "53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1\n", mock_out.getvalue())

    def test_has_digit_in_correct_place(self):
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(123, 123))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(923, 123))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(123, 923))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(123, 199))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(123, 425))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(123, 673))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(199, 123))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(425, 123))
        self.assertTrue(P06MoreGuessing.has_digit_in_correct_place(673, 123))

        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(123, 456))
        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(123, 312))
        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(123, 231))
        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(123, 331))
        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(456, 123))
        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(312, 123))
        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(231, 123))
        self.assertFalse(P06MoreGuessing.has_digit_in_correct_place(331, 123))

    def test_has_same_digit(self):
        self.assertTrue(P06MoreGuessing.has_same_digit(123, 123))
        self.assertTrue(P06MoreGuessing.has_same_digit(923, 123))
        self.assertTrue(P06MoreGuessing.has_same_digit(123, 312))
        self.assertTrue(P06MoreGuessing.has_same_digit(123, 991))
        self.assertTrue(P06MoreGuessing.has_same_digit(123, 299))
        self.assertTrue(P06MoreGuessing.has_same_digit(123, 939))
        self.assertTrue(P06MoreGuessing.has_same_digit(312, 123))
        self.assertTrue(P06MoreGuessing.has_same_digit(991, 123))
        self.assertTrue(P06MoreGuessing.has_same_digit(299, 123))
        self.assertTrue(P06MoreGuessing.has_same_digit(939, 123))

        self.assertFalse(P06MoreGuessing.has_same_digit(123, 456))
        self.assertFalse(P06MoreGuessing.has_same_digit(123, 789))
        self.assertFalse(P06MoreGuessing.has_same_digit(123, 444))
        self.assertFalse(P06MoreGuessing.has_same_digit(456, 123))
        self.assertFalse(P06MoreGuessing.has_same_digit(789, 123))
        self.assertFalse(P06MoreGuessing.has_same_digit(444, 123))

    def test_product_of_terms(self):
        self.assertAlmostEqual(2.0000000, P02ApproximatePi.product_of_terms(1))
        self.assertAlmostEqual(1.3333333, P02ApproximatePi.product_of_terms(2))
        self.assertAlmostEqual(1.7777778, P02ApproximatePi.product_of_terms(3))
        self.assertAlmostEqual(1.4222222, P02ApproximatePi.product_of_terms(4))
        self.assertAlmostEqual(1.7066667, P02ApproximatePi.product_of_terms(5))
        self.assertAlmostEqual(1.4628571, P02ApproximatePi.product_of_terms(6))
        self.assertAlmostEqual(1.6718367, P02ApproximatePi.product_of_terms(7))


if __name__ == '__main__':
    unittest.main()
