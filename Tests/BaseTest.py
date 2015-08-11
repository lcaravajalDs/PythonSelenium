import unittest

#from Config.ConfigParser import parser
from Config.ConfigParser import parser

class BaseTest(unittest.TestCase):
    configfile=parser()
    def setUp(self):
        self.driver = self.configfile.getBrowser('1')
        self.driver.implicitly_wait(10)
        env=self.configfile.get_url()
        self.driver.get(env)

    def tearDown(self):
        self.driver.close()
