import unittest

from service.test_login_page import TestLoginPage

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
    unittest.TextTestRunner(verbosity=1).run(suite)
