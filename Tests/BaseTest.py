import unittest

#from Config.ConfigParser import parser
from Config.ConfigParser import parser
import datetime

class BaseTest(unittest.TestCase):
    configfile=parser()
    def setUp(self):
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        self.driver = self.configfile.getBrowser('1')
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        self.driver.implicitly_wait(10)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        env=self.configfile.get_url()
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        self.driver.get(env)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        

    def tearDown(self):
        self.driver.close()
