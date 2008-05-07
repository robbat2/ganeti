#!/usr/bin/python
#

# Copyright (C) 2006, 2007, 2008 Google Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 0.0510-1301, USA.


"""Script for unittesting the constants module"""


import unittest

from ganeti import constants


class TestConstants(unittest.TestCase):
  """Constants tests"""

  def testConfigVersion(self):
    self.failUnless(constants.CONFIG_MAJOR >= 0 and
                    constants.CONFIG_MAJOR <= 99)
    self.failUnless(constants.CONFIG_MINOR >= 0 and
                    constants.CONFIG_MINOR <= 99)
    self.failUnless(constants.CONFIG_REVISION >= 0 and
                    constants.CONFIG_REVISION <= 9999)
    self.failUnless(constants.CONFIG_VERSION >= 0 and
                    constants.CONFIG_VERSION <= 99999999)


if __name__ == '__main__':
  unittest.main()
