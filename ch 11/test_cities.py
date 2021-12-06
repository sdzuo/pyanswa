import unittest
from city_functions import city_country

#must use a class with unittest before defining the method
class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        #check if LA, California works

        testcc = city_country('tokyo','japan','40 million')
        self.assertEqual(testcc, 'Tokyo, Japan - Population 40 Million')

#run the test case
if __name__ == '__main__':
    unittest.main()
