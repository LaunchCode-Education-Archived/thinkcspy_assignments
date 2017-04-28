from .solution import is_Leap
import unittest

class TestChapter06(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(is_Leap(1944), True)

    def test_solution_02(self):
        self.assertEqual(is_Leap(2011), False)
    
    def test_solution_03(self):
        self.assertEqual(is_Leap(1986), False)

    def test_solution_04(self):
        self.assertEqual(is_Leap(1956), True)

    def test_solution_05(self):
        self.assertEqual(is_Leap(1800), False)
    		
    def test_solution_06(self):
        self.assertEqual(is_Leap(1600), True)
