import unittest
from jaktestowacDemoTests.tests.lost_hat_login_page_pom_tests import LostHatLoginPagePomTests


def full_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(unittest.makeSuite(LostHatLoginPagePomTests))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())