from .solution import find_average
import unittest

class TestChapter10(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(find_average([19,3,1,8,13]), 8)

    def test_solution_02(self):
        self.assertEqual(find_average([0,7,3,4,5,13,1]), 4)

    def test_solution_03(self):
        self.assertEqual(find_average([120,30,50]), 50) 

    		
    	
