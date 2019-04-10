import unittest

from city_function import get_city_country
from city_function import AnonymouseSurvey


class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        tests = get_city_country('Hubei', 'china')
        self.assertEqual(tests, 'Hubei, china')

    def test_city_country_population(self):
        tests = get_city_country('hubei', 'china', 100000)
        self.assertEqual(tests, "hubei, china - population 100000")

    def test_store_single_response(self):
        tests = AnonymouseSurvey("what language do you like?")
        tests.store_response('english')
        self.assertIn('english', tests.responses)


unittest.main()
