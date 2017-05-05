# Test Part 3 of Crypto assignment.
from . import vigenere_final
from . import caesar_final
import unittest


class TestCrypto(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(caesar_final.encrypt("a", 13), "n") 

    def test_solution_2(self):
        self.assertEqual(caesar_final.encrypt("LaunchCode", 13), "YnhapuPbqr")

    def test_solution_3(self):
        self.assertEqual(caesar_final.encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_solution_4(self):
        self.assertEqual(vigenere_final.encrypt("The crow flies at midnight!", "boom"), "Uvs osck rmwse bh auebwsih!")

    def test_solution_5(self):
        self.assertEqual(vigenere_final.encrypt("The crow flies at midnight!", "LaunchCode"), "Ehy ptvy tomps ug opfblkst!")

    def test_solution_6(self):
        self.assertEqual(vigenere_final.encrypt("Wow. This TOTALLY rocks: #CodingRocks", "enthusiasm"), "Abp. Abaa TGFEYEF lgkkk: #OsqbuaJwcce")


    	
