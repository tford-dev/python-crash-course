import unittest;
from city_functions import *;

"""
11-1. City, Country: Write a function that accepts two parameters: a city name and a country
name. The function should return a single string of the form City, Country, such as
Santiago, Chile. Store the function in a module called city_functions.py.
Create a file called test_cities.py that tests the function you just wrote (remember that you
need to import unittest and the function you want to test). Write a method called
test_city_country() to verify that calling your function with values such as 'santiago' and
'chile' results in the correct string. Run test_cities.py, and make sure test_city_country()
passes.


"""
class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_formatted = city_country('richmond', 'united states');
        self.assertEqual(city_country_formatted, 'Richmond, United States.');
    def test_city_country_population(self):
        population_string = city_country_pop('richmond', 'united states', 226604);
        self.assertEqual(population_string, 'Richmond, United States has a population of 226604.')

if __name__ == '__main__':
    unittest.main();