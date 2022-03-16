import unittest
import aos_methods as methods
import aos_locators as locators


class AOSTestCases(unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.setup()
        methods.createnewuser()
        methods.log_out()
        methods.checkhomepagetextsandlinks()
        methods.checktopnav()
        methods.checklogo()
        methods.checkcontactform()
        methods.checksocialmedialinks()
        methods.log_in()
        methods.checkout_shopping()
        methods.log_out()
        methods.tearDown()
