import unittest
from city_country import city_country

class CityCountryTest(unittest.TestCase):
    def test_city_country(self):
        result = city_country('santigo', 'chile')
        self.assertEqual(result, 'Santigo, Chile')
        
    def test_city_country_population(self):
        result = city_country('santigo', 'chile', population=5000)
        self.assertEqual(result, 'Santigo, Chile - population 5000')
        
unittest.main()
