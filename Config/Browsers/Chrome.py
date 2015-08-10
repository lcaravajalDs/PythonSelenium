'''
Created on 7/8/2015

@author: Luciano
'''
import configparser
import os
root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
root_dir=os.path.split(root_dir)[0]+"\\config.ini"
config= configparser.ConfigParser()
config.read(root_dir)
config.set("Browser", '1', "Chrome")
with open(root_dir, 'w') as configfile:    # save
    config.write(configfile)