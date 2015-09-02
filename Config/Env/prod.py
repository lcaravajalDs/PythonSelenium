'''
Created on 7/8/2015

@author: Luciano
'''
from Config.ConfigParser import parser
conf=parser()
conf.setConfig("SUT", '1', "prod")
conf.saveConfigFile()