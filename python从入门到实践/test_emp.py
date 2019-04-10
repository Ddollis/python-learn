import unittest

from employee import Employee


class test_emp(unittest.TestCase):
    def setUp(self):
        self.in1 = Employee('qin', 'di', 0)
        self.in2 = Employee('wang', 'ning', 10)
        self.in1.give_raise()
        self.in2.give_raise(10)

    def test_given_default_raise(self):
        self.assertEqual(5000, self.in1.salay)

    def test_give_cunstom_raise(self):
        self.assertEqual(20, self.in2.salay)


unittest.main()
