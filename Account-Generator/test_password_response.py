import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails

class ResponseTest(unittest.TestCase,UserAccountDetails):

	checker = UserAccountDetails()

	def test_check(self):
		self.assertEquals(self.checker.create_new_user("test_username","test_firstname","test_lastname", "1997", "7$!5I6c2-F1r7m1S"), "You have been successfully added to the database system.") # testing for password
	def test_check1(self):
			self.assertEqual(self.checker.create_new_user("test_username","test_firstname","test_lastname", "1997", "password"), "Your password is weak.") # testing for password

	def test_check2(self):
		self.assertEqual(UserAccountDetails().create_new_user( "Afshana", "Afshana", "Begum", "1997", "password"), "Your password is weak.") # test checks is user details are in password

	def test_check3(self):
		self.assertEqual(self.checker.create_new_user("Afshana_username","Afshana", "Begum", "1997", "s$Y9h70OXO)nXb7Y"), "You have been successfully added to the database system.")

# Test file returning 100% success rate