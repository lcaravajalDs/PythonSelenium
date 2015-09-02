import configparser

from selenium import webdriver
import os

class parser():
    config= configparser.ConfigParser()
    root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]+"//Config//config.ini"
    
    def __init__(self):
        self.config.read(self.root_dir)
        
    def getBrowser(self,param):
        browser=self.config.get("Browser", param)
        print("Opening "+browser)
        if browser == 'Chrome' :
            return webdriver.Chrome('c://Python34//chromedriver')
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
    
    def setConfig(self,section,opt,value):
        self.config.set(section, opt, value)
    
    def saveConfigFile(self):
        with open(self.root_dir, 'w') as configfile:    # save
            self.config.write(configfile)
    
        
