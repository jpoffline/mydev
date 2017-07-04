""" Module containing unit tests for the serverHelp module """
# pylint: disable=C0111
# pylint: disable=C0103

import serverhelp as srv
import tests.test_framework as test


def test_gen_response_string():
    send = '/send'
    keys = ['one', 'two']
    values = ['1', '2']
    expected = '/send?one=1&two=2'

    actual = srv.gen_response_string(send, keys, values)
    return test.exe_test(actual, expected)


def test_Multi_deconstruct_response_string():
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

    return test.exe_test(actual, expected)


def test_Single_deconstruct_response_string():
    test_str = '/send2?your_name=jonny'

    expected = [
        '/send2',
        {
            'key': 'your_name',
            'val': 'jonny'
        }
    ]

    actual = srv.deconstruct_response_string(test_str)

    return test.exe_test(actual, expected)


def test_gen_post_string():
    send = 'id'
    values = ['var1', 'var2']
    actual = srv.gen_post_string(send, values)
    expected = '/id?var1&var2'
    return test.exe_test(actual, expected)
