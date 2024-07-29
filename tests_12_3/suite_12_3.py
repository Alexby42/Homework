import unittest
import tests_12_2, tests_12_3
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.Test))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.Test))
test_runer = unittest.TextTestRunner(verbosity=2)
test_runer.run(test_suite)