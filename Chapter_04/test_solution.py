from .solution import square
import unittest

class TestChapter04(unittest.TestCase):

    def test_solution(self):
    	self.assertEqual(square([2, 3, 4, 6, 9, 10, 15, 20]), [4, 9, 16, 36, 81, 100, 225, 400])

    		
    	
