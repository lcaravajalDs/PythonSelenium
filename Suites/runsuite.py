import unittest
from Tests.test_PythonTestRun import PythonOrgSearch
loader=unittest.defaultTestLoader
suiteToRun=loader.loadTestsFromTestCase(PythonOrgSearch)
runner=unittest.TextTestRunner(verbosity=2)
result=runner.run(suiteToRun)