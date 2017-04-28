from .solution import Point
import unittest

class TestChapter13(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(Point(4, 10).slope_from_origin(), 2.5)

    def test_solution_02(self):
        self.assertEqual(Point(5, 10).slope_from_origin(), 2)
    		
    def test_solution_03(self):
        self.assertEqual(Point(0, 10).slope_from_origin(), None)

    def test_solution_04(self):
        self.assertEqual(Point(20, 20).slope_from_origin(), 1)

    def test_solution_05(self):
        self.assertEqual(Point(4, -10).slope_from_origin(), -2.5)

    def test_solution_06(self):
        self.assertEqual(Point(-4, -10).slope_from_origin(), 2.5)

    def test_solution_07(self):
        self.assertEqual(Point(-6, 0).slope_from_origin(), 0)    		
    	
