from .solution import get_country_codes
import unittest

class TestChapter11(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")

    def test_solution_02(self):
        self.assertEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP") 

    def test_solution_03(self):
        self.assertEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES") 

    def test_solution_04(self):
        self.assertEqual(get_country_codes("CA$40"), "CA") 

    		
    	
