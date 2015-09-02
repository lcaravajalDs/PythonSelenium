import unittest
from Tests.test_PythonTestRun import PythonOrgSearch
import sys
from AnotherTest import AnotherTest
loader=unittest.defaultTestLoader
suiteToRun= unittest.TestSuite([loader.loadTestsFromTestCase(PythonOrgSearch),
                                loader.loadTestsFromTestCase(AnotherTest)
                                ])
xml_msg = ""
try:
    import xmlrunner
    xml_dir = 'test-reports'
    res = xmlrunner.XMLTestRunner(output=xml_dir, verbosity=2).run(suiteToRun)
    xml_msg = ", XML output of tests available in %s directory" % xml_dir
except :
    sys.stderr.write("WARNING: xmlrunner module not available, falling back to using unittest...\n\n")
    res = unittest.TextTestRunner().run(suiteToRun)