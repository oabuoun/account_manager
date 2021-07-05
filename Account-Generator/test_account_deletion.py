# delete account I have created

import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails


# use mock  package to run tests
class PassTest(unittest.TestCase):
    checker = UserAccountDetails()

    def test_delete_account(self):
        self.assertEqual(self.checker.delete_user("test_user", "admin", "admin"),"The account {} has been deleted from the database".format("test_user"))
    #check if the database has been updated
    def test_check_deletion(self):
        self.assertFalse(self.checker.check_existence("username"))
    #check if the account no longer exists
    def test_extra_check_deletion(self):
        self.assertEqual(self.checker.delete_user("Random_user", "admin", "admin"), "The user you are trying to delete isn't on the database")
        self.assertEqual(self.checker.delete_user("Random_user", "no_admin", "admin"),"You require an admin level account to delete user details.")

# 100% pass rate no issues