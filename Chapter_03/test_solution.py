from .solution import hello
import unittest

class TestChapter03(unittest.TestCase):

	def test_solution(self):
		self.assertEqual(hello(), "Hello Chris") # this should fail

	def test_solution2(self):
		self.assertEqual(hello(), "Hello world") # this should pass

