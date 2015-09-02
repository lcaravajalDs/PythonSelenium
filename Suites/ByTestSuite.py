import unittest
from Tests.test_PythonTestRun import PythonOrgSearch
from Tests.AnotherTest import AnotherTest
#Prepare Suite
suiteToRun=unittest.TestSuite()
suiteToRun.addTest(PythonOrgSearch('test_search_in_python_org'))
suiteToRun.addTest(AnotherTest('test_search_in_python_org_Another'))

#Run suite
runner=unittest.TextTestRunner(verbosity=2)
result=runner.run(suiteToRun)
'''
Created on 2/9/2015

@author: Luciano
'''
