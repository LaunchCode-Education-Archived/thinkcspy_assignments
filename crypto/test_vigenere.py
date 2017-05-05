# Test Part 2 of Crypto assignment.
from .vigenere import alphabet_position, rotate_character, encrypt
import unittest


class TestVigenere(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(alphabet_position("b"), 1) 

    def test_solution_2(self):
        self.assertEqual(alphabet_position("C"), 2)

    def test_solution_3(self):
        self.assertEqual(alphabet_position("Z"), 25)

    def test_solution_4(self):
        self.assertEqual(rotate_character(" ", 45), " ")

    def test_solution_5(self):
        self.assertEqual(rotate_character("A", 14), "O")

    def test_solution_6(self):
        self.assertEqual(rotate_character("z", 52), "z")

    def test_solution_7(self):
        self.assertEqual(encrypt("The crow flies at midnight!", "boom"), "Uvs osck rmwse bh auebwsih!")

    def test_solution_8(self):
        self.assertEqual(encrypt("The crow flies at midnight!", "LaunchCode"), "Ehy ptvy tomps ug opfblkst!")

    def test_solution_9(self):
        self.assertEqual(encrypt("Wow. This TOTALLY rocks: #CodingRocks", "enthusiasm"), "Abp. Abaa TGFEYEF lgkkk: #OsqbuaJwcce")

