

import inspect
import sys
from tests.servicetests.test_timer import *
from tests.servicetests.tests_sqllite import *
import tests.test_framework as testframework

from lib.timer import Timer
import time


def some_magic(mod):
    """ Collect together the test functions in the loaded modules """
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    results = []
    for key, _ in all_functions:
        if key.startswith("test_"):

            var = eval(key + '()')  # pylint: disable=W0123

            results.append(var)
    return results


def run_service_tests(args):
    """ Run the unit tests """
    if '-quiet' in args:
        verbose = False
    else:
        verbose = True
    timer = Timer(time)
    if verbose:
        print test.unit_tests_banner(testtype='service')
    timer.start()
    timer.sig(4)
    results = some_magic(sys.modules[__name__])
    timer.end()
    if test.analyse_tests(results, verbose=verbose) is False:
        print 'FAIL'

    if verbose:
        print test.elapsed(timer.elapsed())
        print test.unit_tests_banner(empty=True)


if __name__ == '__main__':
    run_service_tests(sys.argv[1:])
