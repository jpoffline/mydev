# pylint: disable=C0111
# pylint: disable=C0103

import tools as tools
import tests.test_framework as test


def test_collapse_dict():

    input_dict = {
        'key': 'value',
        'key2': 'val'
    }

    actual = tools.collapse_dict(input_dict)
    expected = "key=\"value\" key2=\"val\""
    return test.exe_test(actual, expected)


def test_collapse_css():
    input_css = {
        'h1': {
            'color': 'blue',
            'weight': 'bold'
        },
        'p': {
            'color': 'red',
            'weight': 'italic'
        }
    }
    actual = tools.collapse_css(input_css)
    expected = "p {color: red; weight: italic;} h1 {color: blue; weight: bold;} "
    return test.exe_test(actual, expected)
