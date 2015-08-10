import unittest

from Config.ConfigParser import parser
from selenium import webdriver

class BaseTest(unittest.TestCase):
        def setUp(self):
        print ('algo')
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.python.org")
        
    def test_lala(self):
        print ('lala')

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
