import unittest
from unittest.mock import patch, Mock
from io import StringIO
import math
import random
import P01NinetyNineBottles
import P02MonteCarloPi
import P03EvenOrOdd
import P04RandomWalk
import P08MoreStars


def mock_turtle(x, y):
    mock = Mock()
    mock.xcor.return_value = x
    mock.ycor.return_value = y
    mock.position.return_value = (x, y)
    mock.distance.return_value = math.sqrt(x ** 2 + y ** 2)
    return mock


class MyTestCase(unittest.TestCase):
    def test_bottles(self):
        self.assertEqual("bottles", P01NinetyNineBottles.bottle_text(0))
        self.assertEqual("bottle", P01NinetyNineBottles.bottle_text(1))
        for i in range(2, 100):
            self.assertEqual("bottles", P01NinetyNineBottles.bottle_text(i))

    def test_verse(self):
        self.assertEqual("""99 bottles of milk on the wall,
99 bottles of milk,
Take one down, pass it around,
98 bottles of milk on the wall!
""", P01NinetyNineBottles.verse(99, "milk"))

        self.assertEqual("""2 bottles of Ginger Ale on the wall,
2 bottles of Ginger Ale,
Take one down, pass it around,
1 bottle of Ginger Ale on the wall!
""", P01NinetyNineBottles.verse(2, "Ginger Ale"))

        self.assertEqual("""1 bottle of water on the wall,
1 bottle of water,
Take one down, pass it around,
0 bottles of water on the wall!
""", P01NinetyNineBottles.verse(1, "water"))

        self.assertEqual("""50 bottles of Root Beer on the wall,
50 bottles of Root Beer,
Take one down, pass it around,
49 bottles of Root Beer on the wall!
""", P01NinetyNineBottles.verse(50, "Root Beer"))

    def test_print_song(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            P01NinetyNineBottles.print_song(5, "water")
            self.assertEqual("""5 bottles of water on the wall,
5 bottles of water,
Take one down, pass it around,
4 bottles of water on the wall!

4 bottles of water on the wall,
4 bottles of water,
Take one down, pass it around,
3 bottles of water on the wall!

3 bottles of water on the wall,
3 bottles of water,
Take one down, pass it around,
2 bottles of water on the wall!

2 bottles of water on the wall,
2 bottles of water,
Take one down, pass it around,
1 bottle of water on the wall!

1 bottle of water on the wall,
1 bottle of water,
Take one down, pass it around,
0 bottles of water on the wall!
""", mock_out.getvalue())

    def test_is_home(self):
        turtle = mock_turtle(0, 0)
        self.assertTrue(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0, 0.4 * P04RandomWalk.STEP_SIZE)
        self.assertTrue(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0.4 * P04RandomWalk.STEP_SIZE, 0)
        self.assertTrue(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0, -0.4 * P04RandomWalk.STEP_SIZE)
        self.assertTrue(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(-0.4 * P04RandomWalk.STEP_SIZE, 0)
        self.assertTrue(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0, 0.6 * P04RandomWalk.STEP_SIZE)
        self.assertFalse(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0.6 * P04RandomWalk.STEP_SIZE, 0)
        self.assertFalse(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0, -0.6 * P04RandomWalk.STEP_SIZE)
        self.assertFalse(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0.5 * P04RandomWalk.STEP_SIZE, 0.5 * P04RandomWalk.STEP_SIZE)
        self.assertFalse(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(-0.5 * P04RandomWalk.STEP_SIZE, -0.5 * P04RandomWalk.STEP_SIZE)
        self.assertFalse(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(0.5 * P04RandomWalk.STEP_SIZE, -0.5 * P04RandomWalk.STEP_SIZE)
        self.assertFalse(P04RandomWalk.is_home(turtle))
        turtle = mock_turtle(-0.5 * P04RandomWalk.STEP_SIZE, 0.5 * P04RandomWalk.STEP_SIZE)
        self.assertFalse(P04RandomWalk.is_home(turtle))

    def test_is_inside_window(self):
        turtle = mock_turtle(0, 0)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(0, P04RandomWalk.HEIGHT / 2)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(P04RandomWalk.WIDTH / 2, 0)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(0, -P04RandomWalk.HEIGHT / 2)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(-P04RandomWalk.WIDTH / 2, 0)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(P04RandomWalk.WIDTH / 2, P04RandomWalk.HEIGHT / 2)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(-P04RandomWalk.WIDTH / 2, -P04RandomWalk.HEIGHT / 2)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(P04RandomWalk.WIDTH / 2, -P04RandomWalk.HEIGHT / 2)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(-P04RandomWalk.WIDTH / 2, P04RandomWalk.HEIGHT / 2)
        self.assertTrue(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(0, P04RandomWalk.HEIGHT / 2 + 1)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(P04RandomWalk.WIDTH / 2 + 1, 0)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(0, -P04RandomWalk.HEIGHT / 2 - 1)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(-P04RandomWalk.WIDTH / 2 - 1, 0)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(P04RandomWalk.WIDTH / 2 + 1, P04RandomWalk.HEIGHT / 2 + 1)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(-P04RandomWalk.WIDTH / 2 - 1, -P04RandomWalk.HEIGHT / 2 - 1)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(P04RandomWalk.WIDTH / 2 + 1, -P04RandomWalk.HEIGHT / 2 - 1)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))
        turtle = mock_turtle(-P04RandomWalk.WIDTH / 2 - 1, P04RandomWalk.HEIGHT / 2 + 1)
        self.assertFalse(P04RandomWalk.is_inside_window(turtle))

    def test_is_even(self):
        for i in range(0, 101, 2):
            self.assertTrue(P03EvenOrOdd.is_even(i))
        for i in range(1, 101, 2):
            self.assertFalse(P03EvenOrOdd.is_even(i))

    def test_sum_two_dice(self):
        for i in range(1000):
            self.assertTrue(2 <= P03EvenOrOdd.sum_two_dice() <= 12)
        random.seed(1331, version=2)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 10)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 8)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 7)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 7)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 8)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 7)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 11)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 11)
        self.assertEqual(P03EvenOrOdd.sum_two_dice(), 6)

    def test_throw_dart(self):
        for i in range(1000):
            x, y = P02MonteCarloPi.throw_dart()
            self.assertTrue(-1 <= x <= 1)
            self.assertTrue(-1 <= y <= 1)
        random.seed(12345, version=2)
        self.assertEqual(P02MonteCarloPi.throw_dart(), (0.41661987254534116, 0.010169169457068361))
        self.assertEqual(P02MonteCarloPi.throw_dart(), (0.8252065092537432, 0.2986398551995928))
        self.assertEqual(P02MonteCarloPi.throw_dart(), (0.3684116894884757, 0.19366134904507426))

    def test_is_in_circle(self):
        self.assertTrue(P02MonteCarloPi.is_in_circle(0, 0))
        self.assertTrue(P02MonteCarloPi.is_in_circle(1, 0))
        self.assertTrue(P02MonteCarloPi.is_in_circle(0, 1))
        self.assertTrue(P02MonteCarloPi.is_in_circle(-1, 0))
        self.assertTrue(P02MonteCarloPi.is_in_circle(0, -1))
        self.assertTrue(P02MonteCarloPi.is_in_circle(0.5, 0.5))
        self.assertTrue(P02MonteCarloPi.is_in_circle(-0.5, -0.5))
        self.assertTrue(P02MonteCarloPi.is_in_circle(math.sqrt(0.5), math.sqrt(0.5)))
        self.assertTrue(P02MonteCarloPi.is_in_circle(math.sqrt(0.5), -math.sqrt(0.5)))
        self.assertTrue(P02MonteCarloPi.is_in_circle(-math.sqrt(0.5), math.sqrt(0.5)))
        self.assertFalse(P02MonteCarloPi.is_in_circle(math.sqrt(0.5001), math.sqrt(0.5001)))
        self.assertFalse(P02MonteCarloPi.is_in_circle(math.sqrt(0.5001), -math.sqrt(0.5001)))
        self.assertFalse(P02MonteCarloPi.is_in_circle(-math.sqrt(0.5001), math.sqrt(0.5001)))
        self.assertFalse(P02MonteCarloPi.is_in_circle(1, 1))
        self.assertFalse(P02MonteCarloPi.is_in_circle(-1, -1))
        self.assertFalse(P02MonteCarloPi.is_in_circle(1, -1))
        self.assertFalse(P02MonteCarloPi.is_in_circle(-1, 1))

    def test_stars(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            P08MoreStars.print_stars(1)
            self.assertEqual(fake_out.getvalue(), "*\n")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            P08MoreStars.print_stars(2)
            self.assertEqual(fake_out.getvalue(), "_*\n***\n")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            P08MoreStars.print_stars(3)
            self.assertEqual(fake_out.getvalue(), """__*
_*.*
*****
""")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            P08MoreStars.print_stars(4)
            self.assertEqual(fake_out.getvalue(), """___*
__*.*
_*...*
*******
""")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            P08MoreStars.print_stars(5)
            self.assertEqual(fake_out.getvalue(), """____*
___*.*
__*...*
_*.....*
*********
""")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            P08MoreStars.print_stars(10)
            self.assertEqual(fake_out.getvalue(), """_________*
________*.*
_______*...*
______*.....*
_____*.......*
____*.........*
___*...........*
__*.............*
_*...............*
*******************
""")


if __name__ == '__main__':
    unittest.main()
