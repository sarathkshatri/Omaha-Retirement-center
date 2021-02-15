import unittest
from unit_tests import mypkg
from unit_tests import resident, maintenanceworker, staff

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.loader.findTestCases(resident))
test_suite.addTest(unittest.loader.findTestCases(maintenanceworker))
test_suite.addTest(unittest.loader.findTestCases(staff))

# Add your individual testcases here


# Wrapping up

unittest.TextTestRunner(verbosity=2).run(test_suite)
driver = mypkg.getOrCreateWebdriver()
driver.close()