import unittest
from Login_Register_test import TestAPI as TestLogin
from Sub_unsub_test import TestSub

if __name__ == '__main__':

    # Create a test suite combining all test cases
    all_tests = unittest.TestSuite()
    all_tests.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestSub)
    ])

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(all_tests)
