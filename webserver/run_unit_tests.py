""" unit test driver """

import inspect, sys
from tests.tests_htmltags import *
from tests.tests_htmlwidgets import *
from tests.tests_serverhelp import *
from tests.tests_htmlgenerator import *


def some_magic(mod):
    """ Collect together the test functions in the loaded modules """
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    results = []
    for key, _ in all_functions:
        if key.startswith("test_"):
            var = eval(key + '()') # pylint: disable=W0123
            results.append(var)
    return results

def run_tests():
    """ Run the unit tests """
    results = some_magic(sys.modules[__name__])
    test.analyse_tests(results)


if __name__ == '__main__':
    run_tests()
