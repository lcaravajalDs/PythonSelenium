import unittest
from Tests.test_PythonTestRun import PythonOrgSearch
from Tests.AnotherTest import AnotherTest
loader=unittest.defaultTestLoader
suiteToRun= unittest.TestSuite([loader.loadTestsFromTestCase(PythonOrgSearch),
                                loader.loadTestsFromTestCase(AnotherTest)
                                ])
runner=unittest.TextTestRunner(verbosity=2)
result=runner.run(suiteToRun)