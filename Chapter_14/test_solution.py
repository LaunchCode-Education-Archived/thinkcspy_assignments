from .solution import BoredChatbot
import unittest

class TestChapter14(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(BoredChatbot("Tom").response("Hello World"), "It is very interesting that you say: 'Hello World'")

    def test_solution_02(self):
        self.assertEqual(BoredChatbot("Tom").response(""), "It is very interesting that you say: ''")

    def test_solution_03(self):
        self.assertEqual(BoredChatbot("Tom").response("Humpty Dumpty sat on a wall. Humpty Dumpty had a great fall." +
        		"All the king's horses and all the king's men..."), "zzz... Oh excuse me, I dozed off reading your essay.")

    def test_solution_04(self):
        self.assertEqual(BoredChatbot("Tom").response("What's up?"), "It is very interesting that you say: 'What's up?'")

    		
    	
