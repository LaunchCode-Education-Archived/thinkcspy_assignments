from .solution import mirror
import unittest

class TestChapter09(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(mirror("good"), "gooddoog")

    def test_solution_02(self):
        self.assertEqual(mirror("Python"), "PythonnohtyP")

    def test_solution_03(self):
        self.assertEqual(mirror(""), "")

    def test_solution_04(self):
        self.assertEqual(mirror("act"), "ACTTCA")


    		
    	
