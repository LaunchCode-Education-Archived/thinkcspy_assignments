# Test Part 1 of Crypto assignment.
from .caesar import alphabet_position, rotate_character, encrypt
import unittest


class TestCaesar(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(alphabet_position("a"), 0) 

    def test_solution_2(self):
        self.assertEqual(alphabet_position("Y"), 24)   

    def test_solution_3(self):
        self.assertEqual(rotate_character("a", 13), "n")

    def test_solution_4(self):
        self.assertEqual(rotate_character("!", 45), "!")

    def test_solution_5(self):
        self.assertEqual(rotate_character("C", 27), "D")

    def test_solution_6(self):
        self.assertEqual(rotate_character("z", 37), "k")

    def test_solution_7(self):
        self.assertEqual(encrypt("a", 13), "n")

    def test_solution_8(self):
        self.assertEqual(encrypt("LaunchCode", 13), "YnhapuPbqr")

    def test_solution_9(self):
        self.assertEqual(encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")
