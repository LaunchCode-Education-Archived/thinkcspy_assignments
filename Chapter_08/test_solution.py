from .solution import analyze_text
import unittest

class TestChapter08(unittest.TestCase):

    def test_solution(self):
        text = "Eeeee"
        answer = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'." 
        self.assertEqual(analyze_text(text), answer)

    def test_solution_02(self):
        text = "Blueberries are tastey!"
        answer = "The text contains 20 alphabetic characters, of which 5 (25.0%) are 'e'."
        self.assertEqual(analyze_text(text), answer)

    def test_solution_03(self):
        text = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
        answer = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
        self.assertEqual(analyze_text(text), answer)
    		
    	
