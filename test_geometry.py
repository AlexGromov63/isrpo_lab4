import unittest
import math
import circle
import square
import rectangle
import triangle

class RectangleTests(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rectangle.area(2.5, 4),10)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_zero(self):
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.perimeter(0, 5), 10)
    def test_negative(self):
        self.assertEqual(rectangle.area(-3, 5), -15)
        self.assertEqual(rectangle.perimeter(-3, 5), 4)

    def test_large(self):
        a = 10**60
        self.assertEqual(rectangle.area(a, a), 10**120)
        self.assertEqual(rectangle.perimeter(a, a), 4 * a)

class CircleTests(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(2.5), 6.25 * math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 6 * math.pi)

    def test_zero(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_negative(self):
        self.assertAlmostEqual(circle.area(-2), 4 * math.pi)
        self.assertAlmostEqual(circle.perimeter(-2), -4 * math.pi)

    def test_large(self):
        r = 10**50
        self.assertTrue(math.isclose(circle.area(r), math.pi * r**2))
        self.assertTrue(math.isclose(circle.perimeter(r), 2 * math.pi * r))


class SquareTests(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(2.5), 6.25)
    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_zero(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    def test_negative(self):
        self.assertEqual(square.area(-4), 16)
        self.assertEqual(square.perimeter(-4), -16)

    def test_large(self):
        a = 10**60
        self.assertEqual(square.area(a), 10**120)
        self.assertEqual(square.perimeter(a), 4 * a)


class TriangleTests(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(3, 5), 7.5)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_zero(self):
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_negative(self):
        self.assertEqual(triangle.area(-4, 6), -12)
        self.assertEqual(triangle.perimeter(-3, 4, 5), 6)

    def test_large(self):
        a = 10**50
        self.assertTrue(math.isclose(triangle.area(a, a), 5 * 10**99))
        self.assertEqual(triangle.perimeter(a, a, a), 3 * a)


if __name__ == "__main__":
    unittest.main()