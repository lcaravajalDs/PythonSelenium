import configparser

from selenium import webdriver
import os

class parser():
    config= configparser.ConfigParser()
    
    def __init__(self):
        root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        self.config.read(root_dir+"//config.ini")
        print(self.config.sections())
        
    def getBrowser(self,param):
        browser=self.config.get("Browser", param)
        print("Opening "+browser)
        if browser == 'Chrome' :
            return webdriver.Chrome()
        elif browser == 'FF':
            return webdriver.Firefox()
        elif browser == 'IE':
            return webdriver.Ie()
    
    def get_url(self):
        SUT=self.config.get("SUT", '1')
        env=self.config.get("Env", SUT)
        print("Navigating to "+env)
        return env
    
    def get_first_browser(self):
        return self.getBrowser('1')
        
