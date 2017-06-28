from htmlgenerator import *
import test_framework as test


def test_errorPage_pick_response_page():
    actual = pick_response_page('TEST_ERROR', None)
    expected = page_error()
    return test.exe_test(actual, expected)


def test_Unknown_pick_response_page():
    actual = pick_response_page('ANY', None)
    expected = page_error()
    return test.exe_test(actual, expected)
