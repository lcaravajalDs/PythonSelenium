import unittest

from Config.ConfigParser import parser


class BaseTest(unittest.TestCase):
    configfile=parser()
    def setUp(self):
        self.driver = self.configfile.getBrowser('1')
        self.driver.implicitly_wait(10)
        env=self.configfile.get_url()
        self.driver.get(env)
    def test_lala(self):
        print ('lala')

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
