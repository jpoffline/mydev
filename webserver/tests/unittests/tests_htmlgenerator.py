# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test

import app.lib.htmlgenerator as htmlgenerator



def test_errorPage_pick_response_page():
    actual = htmlgenerator.pick_response_page('TEST_ERROR', None)
    expected = htmlgenerator.page_error()
    return test.exe_test(actual, expected)

