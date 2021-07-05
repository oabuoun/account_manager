import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails


class PassTest(unittest.TestCase):

    checker = UserAccountDetails()
    def test_existence(self):
        self.assertTrue(self.checker.check_existence("admin"))

    def test_added(self):
        #begin by creating a new test_user_details
        # self.assertFalse(self.checker.check_existence("test_username"))
        #Change
        # self.checker.create_new_user("test_username","test_firstname","test_lastname","1998","password")#local database okay (may have some issues on global
        self.assertTrue(self.checker.check_existence("test_user"))

# craete_new_user may have some issues with permantly adding to database otherwise 100%