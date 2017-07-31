# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
import unittest
from context import app


import app.lib.services.hostinfo as hostinfo



class ServiceTestHostInfo(unittest.TestCase):


    def test_compact_datetime_format(self):
        actual = hostinfo.compact_datetime_format()
        expected = '%Y%m%d%H%M%S'
        self.assertEqual(actual, expected)

    def test_pretty_datetime_format(self):
        actual = hostinfo.pretty_datetime_format()
        expected = '%Y-%m-%d %H:%M:%S'
        self.assertEqual(actual, expected)

    def test_TrueCustom_is_string_a_datetime(self):
        tmp = '20170901125412'
        actual = hostinfo.is_string_a_datetime(tmp, fmt=hostinfo.compact_datetime_format())
        expected = True
        self.assertEqual(actual, expected)

    def test_True_is_string_a_datetime(self):
        tmp = '2017-09-01 12:54:12'
        actual = hostinfo.is_string_a_datetime(tmp)
        expected = True
        self.assertEqual(actual, expected)

    def test_False_is_string_a_datetime(self):
        tmp = '201-09-01 12:54:12'
        actual = hostinfo.is_string_a_datetime(tmp)
        expected = False
        self.assertEqual(actual, expected)

    def test_FalseCustom_is_string_a_datetime(self):
        tmp = '2010901125412'
        actual = hostinfo.is_string_a_datetime(tmp, fmt=hostinfo.compact_datetime_format())
        expected = False
        self.assertEqual(actual, expected)