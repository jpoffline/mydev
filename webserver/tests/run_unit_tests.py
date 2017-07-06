""" unit test driver """

import inspect
import sys
import time
#from context import app
import test_framework as test
from unittests.tests_htmltags import *
from unittests.tests_htmlwidgets import *
from unittests.tests_serverhelp import *
from unittests.tests_htmlgenerator import *
from unittests.tests_tools import *
from unittests.tests_ajax_factories import *
from unittests.tests_qy_factories import *
from app.lib.tools.timer import Timer


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
