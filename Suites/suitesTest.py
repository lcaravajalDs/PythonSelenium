import unittest
from Tests.test_PythonTestRun import PythonOrgSearch
loader=unittest.defaultTestLoader
suiteToRun=loader.loadTestsFromTestCase(PythonOrgSearch)
runner=unittest.TextTestRunner(verbosity=0)
result=runner.run(suiteToRun)

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