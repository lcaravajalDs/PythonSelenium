import unittest

#from Config.ConfigParser import parser
from selenium import webdriver



class BaseTest(unittest.TestCase):
    configfile=parser()
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.python.org")

    def tearDown(self):
        self.driver.close()
