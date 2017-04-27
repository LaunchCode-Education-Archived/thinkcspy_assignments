from .solution import calculate_temp
import unittest


class TestChapter03(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(calculate_temp(49), 89)

    def test_solution_2(self):
        self.assertEqual(calculate_temp(50), 40)

    def test_solution_3(self):
        self.assertEqual(calculate_temp(0), 40)

    def test_solution_4(self):
        self.assertEqual(calculate_temp(201), 41)

    def test_solution_5(self):
        self.assertEqual(calculate_temp(-1), 89)
