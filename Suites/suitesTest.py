import unittest
from Tests.test_PythonTestRun import PythonOrgSearch
import sys
loader=unittest.defaultTestLoader
suiteToRun=loader.loadTestsFromTestCase(PythonOrgSearch)
#runner=unittest.TextTestRunner(verbosity=2)
#result=runner.run(suiteToRun)

xml_msg = ""
try:
    import xmlrunner
    xml_dir = 'test-reports'
    res = xmlrunner.XMLTestRunner(output=xml_dir, verbosity=2).run(suiteToRun)
    xml_msg = ", XML output of tests available in %s directory" % xml_dir
except :
    sys.stderr.write("WARNING: xmlrunner module not available, falling back to using unittest...\n\n")
    res = unittest.TextTestRunner().run(suiteToRun)

"""
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
"""