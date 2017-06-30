""" unit test driver """

import inspect
import sys
from tests.tests_htmltags import *
from tests.tests_htmlwidgets import *
from tests.tests_serverhelp import *
from tests.tests_htmlgenerator import *
from tests.tests_tools import *
from lib.timer import Timer
import time


def some_magic(mod):
    """ Collect together the test functions in the loaded modules """
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    results = []

    timer = Timer(time)
    timer.sig(5)
    for key, _ in all_functions:
        if key.startswith("test_"):
            timer.start()
            var = eval(key + '()')  # pylint: disable=W0123
            timer.end()
            timer.save(key, reset=True)
            results.append(var)
    timer.sort_laps()
    timer.print_stats()
    return results


def run_tests():
    """ Run the unit tests """
    timer = Timer(time)
    print test.unit_tests_banner()
    timer.start()
    timer.sig(4)
    results = some_magic(sys.modules[__name__])
    timer.end()
    test.analyse_tests(results)
    print test.elapsed(timer.elapsed())
    print test.unit_tests_banner(True)


if __name__ == '__main__':
    run_tests()
