'''
Created on 7/8/2015

@author: Luciano
'''
import unittest


class AnotherTest(unittest.TestCase):

    def test_name(self):
        assert 2 in [1,3]

def suite():

    suite = unittest.TestSuite()

    suite.addTest (AnotherTest())

    return suite