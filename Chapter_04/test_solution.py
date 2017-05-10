from .solution import sum_squares
import unittest

class TestChapter04(unittest.TestCase):

    def test_solution(self):
    	self.assertEqual(sum_squares([2, 3, 4, 6, 9, 10, 15, 20]), 871)

    		
    	
