# Copyright (c) 2025, 1TeamDigital and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestGroup(UnitTestCase):
	"""
	Unit tests for Group.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestGroup(IntegrationTestCase):
	"""
	Integration tests for Group.
	Use this class for testing interactions between multiple components.
	"""

	pass
