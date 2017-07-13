""" Module containing unit tests for the serverHelp module """
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import app.lib.tools.serverhelp as srv
import unittest


class TestServerhelp(unittest.TestCase):

    def setUp(self):
        class tmp(object):
            def __init__(self, val):
                self.value = val
        self.mock_form = tmp

    def test_gen_response_string(self):
        send = '/send'
        keys = ['one', 'two']
        values = ['1', '2']
        expected = '/send?one=1&two=2'

        actual = srv.gen_response_string(send, keys, values)
        self.assertEqual(actual, expected)

    def test_Multi_deconstruct_response_string(self):
        test_str = '/send2?your_name=jonny&your_age=29'

        expected = [
            '/send2',
            {
                'key': 'your_name',
                'val': 'jonny'
            },
            {
                'key': 'your_age',
                'val': '29'
            }
        ]

        actual = srv.deconstruct_response_string(test_str)

        self.assertEqual(actual, expected)

    def test_Single_deconstruct_response_string(self):
        test_str = '/send2?your_name=jonny'

        expected = [
            '/send2',
            {
                'key': 'your_name',
                'val': 'jonny'
            }
        ]

        actual = srv.deconstruct_response_string(test_str)

        self.assertEqual(actual, expected)

    def test_gen_post_string(self):
        send = 'id'
        values = ['var1', 'var2']
        actual = srv.gen_post_string(send, values)
        expected = '/id?var1&var2'
        self.assertEqual(actual, expected)

    def test_False_read_form(self):

        form = {'one': 2}
        key = 'two'
        actual = srv.read_form(form, key)
        expected = 'False'
        self.assertEqual(actual, expected)

    def test_Inside_read_form(self):

        form = {'one': self.mock_form(2)}
        key = 'one'
        actual = srv.read_form(form, key)
        expected = 2
        self.assertEqual(actual, expected)

    def test_Empty_read_form(self):

        form = {'one': self.mock_form('')}
        key = 'one'
        actual = srv.read_form(form, key)
        expected = 'empty'
        self.assertEqual(actual, expected)
        