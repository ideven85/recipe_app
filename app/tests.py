"""
Sample Test Case
"""

from django.test import SimpleTestCase
import calc


class CalcTest(SimpleTestCase):

    def test_calc_add(self):
        x = 1
        y = 2
        self.assertEqual(calc.add(x, y), 3)

    def test_calc_sub(self):
        x = 1
        y = 2
        self.assertEqual(calc.sub(x, y), -1)
