import unittest

from Config.ConfigParser import parser


class BaseTest(unittest.TestCase):
    configfile=parser()
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.python.org")
        
    def test_lala(self):
        print ('lala')

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
