from .solution import is_prime
import unittest

class TestChapter07(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(is_prime(1), False)

    def test_solution_02(self):
        self.assertEqual(is_prime(5), True)

    def test_solution_03(self):
        self.assertEqual(is_prime(8), False)

    def test_solution_04(self):
        self.assertEqual(is_prime(199), True)         

    def test_solution_05(self):
        self.assertEqual(is_prime(144), False)

    def test_solution_06(self):
        self.assertEqual(is_prime(2), True) 

    def test_solution_07(self):
        self.assertEqual(is_prime(-19), False) 
    		
    	
