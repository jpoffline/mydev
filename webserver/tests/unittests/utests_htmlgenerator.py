# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
import unittest
from context import app
import app.lib.tools.htmlgenerator as htmlgenerator


class TestHtmlgenerator(unittest.TestCase):

    def test_errorPage_pick_response_page(self):
        actual = htmlgenerator.pick_response_page('TEST_ERROR', None)
        expected = htmlgenerator.page_error()
        self.assertEqual(actual, expected)
