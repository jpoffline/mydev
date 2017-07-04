from htmlgenerator import *
import tests.test_framework as test


def test_errorPage_pick_response_page():
    actual = pick_response_page('TEST_ERROR', None)
    expected = page_error()
    return test.exe_test(actual, expected)

