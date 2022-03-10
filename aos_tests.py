import unittest
import aos_methods as methods
import aos_locators as locators


class AOSTestCases(unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.createnewuser()
        methods.log_out()
        methods.log_in()
        methods.log_out()
        methods.tearDown()
