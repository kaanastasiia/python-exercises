import unittest
from city_functions import get_city_country

class CityCountryTest(unittest.TestCase):
    def test_city_country(self):
        city_and_country = get_city_country("Zurich", "Switzerland")
        self.assertEqual(city_and_country, 'Zurich, Switzerland')

class CityCountryPopulationTest(unittest.TestCase):
    def test_city_country_population(self):
        city_coutry_and_population = get_city_country("Athens","Greece","2400000")
        self.assertEqual(city_coutry_and_population, "Athens, Greece - Population 2400000" )

if __name__== '__main__':
    unittest.main()

