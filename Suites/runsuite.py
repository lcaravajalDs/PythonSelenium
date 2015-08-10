import unittest
from Suites import suitesTest
def runner():
    allsuites= [suitesTest.suite()]
    unittest.TextTestRunner().run(allsuites)