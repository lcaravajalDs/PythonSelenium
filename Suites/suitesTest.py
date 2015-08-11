import unittest
from Tests.test_PythonTestRun import PythonOrgSearch
import datetime
current_time = datetime.datetime.now().time()
print (current_time.isoformat())
print ("Starting Suite")
loader=unittest.defaultTestLoader
current_time = datetime.datetime.now().time()
print (current_time.isoformat())
suiteToRun=loader.loadTestsFromTestCase(PythonOrgSearch)
current_time = datetime.datetime.now().time()
print (current_time.isoformat())
runner=unittest.TextTestRunner(verbosity=2)
current_time = datetime.datetime.now().time()
print (current_time.isoformat())
result=runner.run(suiteToRun)
current_time = datetime.datetime.now().time()
print (current_time.isoformat())
print ('')
print ("---- START OF TEST RESULTS")
print (result)
print ('')
print ('')
print ('')
print ("result::errors")
print (result.errors)
print ('')
print ('')
print ('')
print ("result::failures")
print (result.failures)
print ('')
print ('')
print ('')
print ("result::skipped")
print (result.skipped)
print ('')
print ('')
print ('')
print ("result::successful")
print (result.wasSuccessful())
print ('')
print ('')
print ('')
print ("result::test-run")
print (result.testsRun)
print ("---- END OF TEST RESULTS")
print ('')
