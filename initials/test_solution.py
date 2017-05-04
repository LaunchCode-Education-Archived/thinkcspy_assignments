from .solution import get_initials
import unittest


class TestInitials(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(get_initials("Ozzie Smith"), "OS") 

    def test_solution_2(self):
        self.assertEqual(get_initials("Bonnie blair"), "BB")   

    def test_solution_3(self):
        self.assertEqual(get_initials("George"), "G")

    def test_solution_4(self):
        self.assertEqual(get_initials("Daniel day Lewis"), "DDL")


    	
