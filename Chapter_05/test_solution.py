from .solution import area_of_circle
import unittest
import math

class TestChapter05(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(area_of_circle(0), 0) 

    def test_solution_2(self):
        self.assertEqual(area_of_circle(1), math.pi)   

    def test_solution_3(self):
        self.assertEqual(area_of_circle(100), 31415.926535897932)

    def test_solution_4(self):
        self.assertEqual(area_of_circle(-1), math.pi)

    def test_solution_5(self):
        self.assertEqual(area_of_circle(-5), 25 * math.pi)

    	
