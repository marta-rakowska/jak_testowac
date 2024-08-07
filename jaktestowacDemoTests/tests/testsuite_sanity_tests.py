import unittest
from jaktestowacDemoTests.tests.lost_hat_login_page_pom_tests import LostHatLoginPagePomTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(LostHatLoginPagePomTests('test_correct_login'))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(sanity_suite())